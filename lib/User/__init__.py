from datetime import datetime
from lib.SqlRunner import SqlRunner
from lib.SecretCrypto import Cryptography
from lib.Validation import Validation

def currentTime():
	now = datetime.now() 
	date_time = now.strftime("%Y-%m-%d %H:%M:%S")
	return date_time

class User:
	def __init__(self):
		pass
		
	def verify(self):
		objSql=SqlRunner("Ledger.sqlite")
		objSql.sql="""
		  Select PublicKey,Name,NID,PreviousHash,EventDate,Char,Level,Description,token from Users
		"""
		data_list=objSql.run()
		
		obj=Cryptography()
		
		for data in data_list:
			publicKey=data[0]
			name=data[1]
			nId=data[2]
			previousHash=data[3]
			eventDate=data[4]
			char=data[5]
			level=data[6]
			description=data[7]
			token=data[8]
			
			dict_data={
			"public_key":publicKey,
			"writer_name":name,
			"nid":nId,
			"description":description,
			"char":char,
			"level":level,
			"event_date":eventDate,
			"previous_hash":previousHash
			}
			
			status=obj.verifyTokenOfHash(data=dict_data,token=token,char=char,level=level)
			
			if(status==False):
				return False
		
		return True
		
	def add(self,name,nId,description,level,char):
		obj=Cryptography()
		keyPair=obj.generateKey()
		publicKey=keyPair["public_key"]
		eventDate=currentTime()
		
		objSql=SqlRunner("Ledger.sqlite")
		objSql.sql="""
		  Select Hash,No from Users
		  ORDER BY No DESC LIMIT 1 
		"""
		previousHash=objSql.run()[0][0]
		no=objSql.run()[0][1]
		
		dict_data={
		"public_key":publicKey,
		"writer_name":name,
		"nid":nId,
		"description":description,
		"char":char,
		"level":level,
		"event_date":eventDate,
		"previous_hash":previousHash
		}
		
		hash_token=obj.getTokenOfHash(dict_data,char,level)
		hash=hash_token["hash"]
		token=hash_token["token"]
		
		sql_code="""
		INSERT INTO Users(No,PublicKey,Name,NID,PreviousHash,Level,Char,Hash,Token,Description,EventDate)
		Values({0},'{1}','{2}','{3}','{4}',{5},'{6}','{7}','{8}','{9}','{10}')
		""".format(no+1,publicKey,name,nId,previousHash,level,char,hash,token,description,eventDate)
		
		objSql.sql=sql_code
		objSql.run()
		
		return keyPair