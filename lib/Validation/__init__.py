from lib.SqlRunner import SqlRunner

class Validation:
	def isPublicKeyExist(self,publicKey):
		
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select No From Users Where PublicKey='{publicKey}'; 
		""".format(publicKey=publicKey)
		
		data_list=objSql.run()
		
		if(len(data_list)==0):
			return False
		
		return True
		
	def isNFTExist(self,nft):
		
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select NFT From NFTs Where NFT='{nft}'; 
		""".format(nft=nft)
		
		data_list=objSql.run()
		
		if(len(data_list)==0):
			return False
		
		return True
		
	
	def isSignatureExist(self,signature):
		
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select Signature From NFTs Where Signature='{signature}'; 
		""".format(signature=signature)
		
		data_list=objSql.run()
		
		if(len(data_list)==0):
			return False
		
		return True