from lib.SqlRunner import SqlRunner
from lib.SecretCrypto import Cryptography
from lib.Validation import Validation
from datetime import datetime

def currentTime():
	now = datetime.now() 
	date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
	return date_time

class Story:
	
	def verify(self):
			
		obj=Cryptography()
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select PublicKey,StoryName,StoryDescription,EventDate,Signature,PreviousHash,Char,Level,Token From Stories;
		"""
		
		data_list=objSql.run()
		
		for data in data_list:
			
			publicKey=data[0]
			storyName=data[1]
			storyDescription=data[2]
			eventDate=data[3]
			signature=data[4]	
			previousHash=data[5]
			char=data[6]
			level=data[7]
			token=data[8]
			
			dict_data={
			"public_key":publicKey,
			"story_name":storyName,
			"story_description":storyDescription,
			"event_date":eventDate,
			"previous_hash":previousHash,
			"signature":signature,
			"char":char,
			"level":level
			}
			
			status=obj.verifyTokenOfHash(data=dict_data,token=token,char=char,level=level)
			
			if(status==False):
				
				return False
		
		return True
		
	
	def add(self,privateKey,storyName,storyDescription,level,char):
		
		obj=Cryptography()
		publicKey=obj.privateKeyToPublicKey(privateKey)
		
		objValid=Validation()
		
		if(objValid.isPublicKeyExist(publicKey)==False):
			raise ValueError("public key is not in the ledger")
		
		objSql=SqlRunner("Ledger.sqlite")
		
		eventDate=currentTime()
		
		objSql.sql="""
		  Select Hash,No from Stories
		  ORDER BY No DESC LIMIT 1 
		"""
		
		previousHash=objSql.run()[0][0]
		no=objSql.run()[0][1]
		
		signature_data={
			"public_key":publicKey,
			"story_name":storyName,
			"story_description":storyDescription,
			"event_date":eventDate,
			"previous_hash":previousHash,
			"char":char,
			"level":level
			}
		
		signature=obj.signData(privateKey,signature_data)
		
		dict_data={
			"public_key":publicKey,
			"story_name":storyName,
			"story_description":storyDescription,
			"event_date":eventDate,
			"previous_hash":previousHash,
			"signature":signature,
			"char":char,
			"level":level
			}
		
		hash_token=obj.getTokenOfHash(dict_data,char,level)
		hash=hash_token["hash"]
		token=hash_token["token"]
		
		sql_code="""
		INSERT INTO Stories(No,PublicKey,StoryName,StoryDescription,Level,Char,PreviousHash,hash,Token,Signature,EventDate)
		
		Values({no},'{publicKey}','{storyName}','{storyDescription}',{level},'{char}','{previousHash}','{hash}',{token},'{signature}','{eventDate}')
		""".format(no=no+1,publicKey=publicKey,level=level,char=char,previousHash=previousHash,hash=hash,token=token,signature=signature,eventDate=eventDate,storyName=storyName,storyDescription=storyDescription)
		
		objSql.sql=sql_code
		objSql.run()
		
		return signature
		
		
	def check_signature(self,publicKey,signature):
		
		objValid=Validation()
		
		if(objValid.isPublicKeyExist(publicKey)==False):
			raise ValueError("public key is not in the ledger")
		
		obj=Cryptography()
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select PublicKey,StoryName,StoryDescription,EventDate,PreviousHash,Char,Level From Stories Where Signature='{signature}'; 
		""".format(signature=signature)
		
		data_list=objSql.run()
		data=data_list[0]
		publicKey=data[0]
		storyName=data[1]
		storyDescription=data[2]
		eventDate=data[3]
		previousHash=data[4]
		char=data[5]
		level=data[6]
		
		dict_data={
			"public_key":publicKey,
			"story_name":storyName,
			"story_description":storyDescription,
			"event_date":eventDate,
			"previous_hash":previousHash,
			"char":char,
			"level":level
			}
		
		status=obj.verifyData(publicKey=publicKey,data=dict_data,signature=signature)
		
		if(status==False):
				return False
			
		return True
		