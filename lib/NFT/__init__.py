from lib.SqlRunner import SqlRunner
from lib.SecretCrypto import Cryptography
from lib.Validation import Validation
from datetime import datetime

def currentTime():
	now = datetime.now() 
	date_time = now.strftime("%Y-%m-%d %H:%M:%S")
	return date_time


class NFT:
	
	def verify(self):
			
		obj=Cryptography()
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select SellerPublicKey,BuyerPublicKey,NFT,FileLocation,EventDate,Signature,hash,Char,Level,Token,Status From NFTs;
		"""
		
		data_list=objSql.run()
		
		i=1
		while (len(data_list)>i):
			
			data=data_list[i]
			sellerPublicKey=data[0]
			buyerPublicKey=data[1]
			nft=data[2]
			fileLocation=data[3]
			eventDate=data[4]
			signature=data[5]
			previousHash=data_list[i-1][6]
			char=data[7]
			level=data[8]
			token=data[9]
			status=data[10]
			
			dict_data={
			"seller_public_key":sellerPublicKey,
			"buyer_public_key":buyerPublicKey,
			"nft":nft,
			"file_location":fileLocation,
			"event_data":eventDate,
			"signature":signature,
			"previous_hash":previousHash,
			"char":char,
			"level":level,
			"status":status,
			}
			
			status=obj.verifyTokenOfHash(data=dict_data,token=token,char=char,level=level)
			
			i+=1
			
			if(status==False):
				
				return False
		
		return True
		
	
	def findOwner(self,nft):
		obj=Cryptography()
		objValid=Validation()
		
		if(objValid.isNFTExist(nft)==False):
			raise ValueError("NFT is not in the ledger")
			
		objSql=SqlRunner("Ledger.sqlite")
		objSql.sql="""
		  SElect 
		  SellerPublicKey,
		  BuyerPublicKey,
		  Token,
		  Signature,
		  Status,
		  Level,
		  Char,
		  FileLocation  
		  from NFTs 
		  Where NFT='{nft}' 
		  Order by datetime(EventDate)  
		  DESC LIMIt 1
		""".format(nft=nft)
		
		data_list=objSql.run()
		if(len(data_list)==0):
			return []
			
		else:
			data=[
			{
			"owner":data_list[0][1],
			"seller_public_key":data_list[0][0],
			"buyer_public_key":data_list[0][1],
			"token":data_list[0][2],
			"signature":data_list[0][3],
			"status":data_list[0][4],
			"level":data_list[0][5],
			"char":data_list[0][6],
			"file_location":data_list[0][7]
				}
			]
			return data
		
	
	def add_nft(self,privateKey,nft,fileLocation,level,char):
		
		obj=Cryptography()
		publicKey=obj.privateKeyToPublicKey(privateKey)
		
		objValid=Validation()
		
		if(objValid.isNFTExist(nft)==True):
			raise ValueError("NFT is already in the ledger")
		
		if(objValid.isPublicKeyExist(publicKey)==False):
			raise ValueError("public key is not in the ledger")
		
		objSql=SqlRunner("Ledger.sqlite")
		
		eventDate=currentTime()
		
		objSql.sql="""
		  Select Hash,No from NFTs
		  ORDER BY No DESC LIMIT 1 
		"""
		
		previousHash=objSql.run()[0][0]
		no=objSql.run()[0][1]
		
		status="nft_added"
		
		signature_data={
			"seller_public_key":publicKey,
			"buyer_public_key":publicKey,
			"nft":nft,
			"file_location":fileLocation,
			"event_data":eventDate,
			"previous_hash":previousHash,
			"char":char,
			"level":level,
			"status":status,
			}
		
		signature=obj.signData(privateKey,signature_data)
		
		dict_data={
			"seller_public_key":publicKey,
			"buyer_public_key":publicKey,
			"nft":nft,
			"file_location":fileLocation,
			"event_data":eventDate,
			"signature":signature,
			"previous_hash":previousHash,
			"char":char,
			"level":level,
			"status":status,
			}
		
		hash_token=obj.getTokenOfHash(dict_data,char,level)
		hash=hash_token["hash"]
		token=hash_token["token"]
		
		sql_code="""
		INSERT INTO NFTs(No,SellerPublicKey,BuyerPublicKey,NFT,Level,Char,Token,FileLocation,Signature,Status,PreviousHash,hash,EventDate)
		Values(
		{no},
		'{publicKey}',
		'{publicKey}',
		'{nft}',
		{level},
		'{char}',
	    {token},
	    '{fileLocation}',
	    '{signature}',
	    '{status}',
	    '{previousHash}',
	    '{hash}',
	    '{eventDate}'
		)
		""".format(no=no+1,publicKey=publicKey,nft=nft,level=level,char=char,token=token,fileLocation=fileLocation,signature=signature,status=status,previousHash=previousHash,hash=hash,eventDate=eventDate)
		
		objSql.sql=sql_code
		objSql.run()
		
		return signature
		
		
	def check_signature(self,sellerPublicKey,signature):
		
		objValid=Validation()
		
		if(objValid.isPublicKeyExist(sellerPublicKey)==False):
			raise ValueError("public key is not in the ledger")
		
		if(objValid.isSignatureExist(signature)==False):
			raise ValueError("signature is not in the ledger")
		
		obj=Cryptography()
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select 
		  BuyerPublicKey,
		  NFT,
		  FileLocation,
		  EventDate,
		  Signature,
		  PreviousHash,
		  Char,
		  Level,
		  Status 
		  From NFTs Where Signature='{signature}';
		""".format(signature=signature)
		
		data_list=objSql.run()
		
		data=data_list[0]
		
		buyerPublicKey=data[0]
		nft=data[1]
		fileLocation=data[2]
		eventDate=data[3]
		signature=data[4]
		previousHash=data[5]
		char=data[6]
		level=data[7]
		status=data[8]
		
		signature_data={
			"seller_public_key":sellerPublicKey,
			"buyer_public_key":buyerPublicKey,
			"nft":nft,
			"file_location":fileLocation,
			"event_data":eventDate,
			"previous_hash":previousHash,
			"char":char,
			"level":level,
			"status":status
			}
		
		status=obj.verifyData(publicKey=sellerPublicKey,data=signature_data,signature=signature)
		
		return status
		
	
	def transfer_nft(self,sellerPrivateKey,buyerPublicKey,nft):
		obj=Cryptography()
		sellerPublicKey=obj.privateKeyToPublicKey(sellerPrivateKey)
		
		objValid=Validation()
		objSql=SqlRunner("Ledger.sqlite")
	
		if(objValid.isPublicKeyExist(sellerPublicKey)==False):
			raise ValueError("seller public key is not in the ledger")
			
		if(objValid.isPublicKeyExist(buyerPublicKey)==False):
			raise ValueError("buyer public key is not in the ledger")
		
		if(objValid.isNFTExist(nft)==False):
			raise ValueError("NFT is not in the ledger")
			
		if(sellerPublicKey==buyerPublicKey):
			raise ValueError("you have the ownership already")
			
		owner_data=self.findOwner(token=nft)[0]
		owner=owner_data["buyer_public_key"]
		level=owner_data["level"]
		char=owner_data["char"]
		fileLocation=owner_data["file_location"]
		
		
		if(sellerPublicKey!=owner):
			raise ValueError("you do not have the ownership ")
		
		eventDate=currentTime()
		
		objSql.sql="""
		  Select Hash,No from NFTs
		  ORDER BY No DESC LIMIT 1 
		"""
		
		previousHash=objSql.run()[0][0]
		no=objSql.run()[0][1]
		
		status="ownership_changed"
		
		signature_data={
			"seller_public_key":sellerPublicKey,
			"buyer_public_key":buyerPublicKey,
			"nft":nft,
			"file_location":fileLocation,
			"event_data":eventDate,
			"previous_hash":previousHash,
			"char":char,
			"level":level,
			"status":status,
			}
		
		signature=obj.signData(sellerPrivateKey,signature_data)
		
		dict_data={
			"seller_public_key":sellerPublicKey,
			"buyer_public_key":buyerPublicKey,
			"nft":nft,
			"file_location":fileLocation,
			"event_data":eventDate,
			"signature":signature,
			"previous_hash":previousHash,
			"char":char,
			"level":level,
			"status":status,
			}
		
		hash_token=obj.getTokenOfHash(dict_data,char,level)
		hash=hash_token["hash"]
		token=hash_token["token"]
		
		sql_code="""
		INSERT INTO NFTs(No,SellerPublicKey,BuyerPublicKey,NFT,Level,Char,Token,FileLocation,Signature,Status,PreviousHash,hash,EventDate)
		Values(
		{no},
		'{sellerPublicKey}',
		'{buyerPublicKey}',
		'{nft}',
		{level},
		'{char}',
	    {token},
	    '{fileLocation}',
	    '{signature}',
	    '{status}',
	    '{previousHash}',
	    '{hash}',
	    '{eventDate}'
		)
		""".format(no=no+1,sellerPublicKey=sellerPublicKey,buyerPublicKey=buyerPublicKey,nft=nft,level=level,char=char,token=token,fileLocation=fileLocation,signature=signature,status=status,previousHash=previousHash,hash=hash,eventDate=eventDate)
		
		objSql.sql=sql_code
		objSql.run()
		
		return signature