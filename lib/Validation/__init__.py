from lib.SqlRunner import SqlRunner

class Validation:
	def isPublicKeyExist(self,publicKey):
		
		objSql=SqlRunner("Ledger.sqlite")
		
		objSql.sql="""
		  Select PublicKey From Writers Where PublicKey='{publicKey}'; 
		""".format(publicKey=publicKey)
		
		data_list=objSql.run()
		
		if(len(data_list)==0):
			return False
		
		return True