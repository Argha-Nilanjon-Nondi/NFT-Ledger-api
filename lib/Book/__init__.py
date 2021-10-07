from lib.SqlRunner import SqlRunner
from lib.SecretCrypto import Cryptography
from datetime import datetime

def currentTime():
	now = datetime.now() 
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	return date_time

class Book:
	
	def verify(self):
			
		obj=Cryptography()
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select PublicKey,BookName,EventDate,Description,Signature,PreviousHash,Char,Level,Token From Books;
		"""
		
		data_list=objSql.run()
		
		for data in data_list:
			
			publicKey=data[0]
			bookName=data[1]
			eventDate=data[2]
			description=data[3]
			signature=data[4]
			previousHash=data[5]
			char=data[6]
			level=data[7]
			token=data[8]
			
			dict_data={
			"public_key":publicKey,
			"book_name":bookName,
			"event_date":eventDate,
			"description":description,
			"previous_hash":previousHash,
			"signature":signature,
			"char":char,
			"level":level
			}
			
			status=obj.verifyTokenOfHash(data=dict_data,token=token,char=char,level=level)
			
			if(status==False):
				
				return False
		
		return True
		
	
	def add(self,privateKey,bookName,description,level,char):
		
		obj=Cryptography()
		publicKey=obj.privateKeyToPublicKey(privateKey)
		
		objSql=SqlRunner("Ledger.sqlite")
		
		eventDate=currentTime()
		
		objSql.sql="""
		  Select Hash,No from Books
		  ORDER BY No DESC LIMIT 1 
		"""
		
		previousHash=objSql.run()[0][0]
		no=objSql.run()[0][1]
		
		signature_data={
			"public_key":publicKey,
			"book_name":bookName,
			"event_date":eventDate,
			"description":description,
			"previous_hash":previousHash,
			"char":char,
			"level":level
		}
		
		signature=obj.signData(privateKey,signature_data)
		
		dict_data={
			"public_key":publicKey,
			"book_name":bookName,
			"event_date":eventDate,
			"description":description,
			"previous_hash":previousHash,
			"signature":signature,
			"char":char,
			"level":level
		}
		
		hash_token=obj.getTokenOfHash(dict_data,char,level)
		hash=hash_token["hash"]
		token=hash_token["token"]
		
		sql_code="""
		INSERT INTO Books(No,PublicKey,BookName,Level,Char,PreviousHash,hash,Token,Signature,EventDate,Description)
		
		Values({no},'{publicKey}','{bookName}',{level},'{char}','{previousHash}','{hash}',{token},'{signature}','{eventDate}','{description}')
		""".format(no=no+1,publicKey=publicKey,bookName=bookName,level=level,char=char,previousHash=previousHash,hash=hash,token=token,signature=signature,eventDate=eventDate,description=description)
		
		objSql.sql=sql_code
		objSql.run()
		
		return signature
		
		
	def check_signature(self,publicKey,signature):
		
		obj=Cryptography()
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select PublicKey,BookName,EventDate,Description,Signature,PreviousHash,Char,Level From Books Where Signature='{signature}'; 
		""".format(signature=signature,publicKey=publicKey)
		
		data_list=objSql.run()
		data=data_list[0]
		publicKey=data[0]
		bookName=data[1]
		eventDate=data[2]
		description=data[3]
		signature=data[4]
		previousHash=data[5]
		char=data[6]
		level=data[7]
		
		dict_data={
		"public_key":publicKey,
		"book_name":bookName,
		"event_date":eventDate,
		"description":description,
		"previous_hash":previousHash,
		"char":char,
		"level":level
		}
		
		status=obj.verifyData(publicKey=publicKey,data=dict_data,signature=signature)
		
		if(status==False):
				return False
			
		return True
		