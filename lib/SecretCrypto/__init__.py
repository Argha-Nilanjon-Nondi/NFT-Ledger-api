from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
from Crypto import Random
import binascii


def getHash(data,num):
	data=str(data)+str(num)
	hash = SHA256.new(data.encode())
	hash_string=hash.hexdigest()
	return hash_string				
						
class Cryptography:
	
	@staticmethod
	def generateKey():
		randnum=Random.new().read
		keyPair = RSA.generate(1024,randnum)
		privateKey=keyPair.export_key().decode()
		publicKey= keyPair.publickey().export_key().decode()
		
		privateKey=binascii.hexlify(privateKey.encode()).decode()
		publicKey=binascii.hexlify(publicKey.encode()).decode()
		
		return {"private_key":privateKey,"public_key":publicKey}
		
	@staticmethod
	def signData(privateKey,data):
		data=str(data)
		privateKey=binascii.unhexlify(privateKey.encode())
		hash = SHA256.new(data.encode())
		privateKey = RSA.importKey(privateKey)
		signer = PKCS115_SigScheme(privateKey)
		signature = signer.sign(hash)
		return binascii.hexlify(signature).decode()
		
	
	@staticmethod
	def verifyData(publicKey,data,signature):
		data=str(data)
		publicKey=binascii.unhexlify(publicKey.encode())
		hash = SHA256.new(data.encode())
		publicKey = RSA.importKey(publicKey)
		verifier = PKCS115_SigScheme(publicKey)
		signature=binascii.unhexlify(signature.encode())
		try:
			verifier.verify(hash, signature)
			return True
		except:
			return False
		
	
	@staticmethod
	def privateKeyToPublicKey(privateKey):
		 privateKey=binascii.unhexlify(privateKey.encode())
		 privateKey = RSA.importKey(privateKey)
		 publicKey=privateKey.publickey().exportKey().decode()
		 publicKey=binascii.hexlify(publicKey.encode()).decode()
		 return publicKey
		
	
	@staticmethod
	def getTokenOfHash(data,char,level=1):
		i=0
		test_hash=getHash("","")
		if(len(test_hash)<level):
			raise ValueError("level must be equal or less than hash length")
		while True:
			hash=getHash(data,i)
			first_n_char=hash[0:level]
			if(first_n_char==(char*level)):
				return {"token":i,"hash":hash}
			i+=1 
			
	@staticmethod
	def verifyTokenOfHash(data,token,char,level=1):
		test_hash=getHash("","")
		if(len(test_hash)<level):
			raise ValueError("level must be equal or less than hash length")
		hash=getHash(data,token)
		first_n_char=hash[0:level]
		verify=(first_n_char==(char*level))
		return verify


#obj=Cryptography()
#keyPair=obj.generateKey()
#privateKey=keyPair["private_key"]
#publicKey=keyPair["public_key"]
#print(keyPair)
#publicKey="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCMCnYWgrXgpXSTJt3tkjKe2Rrf v6LP5pXVTleJhDuSaAw3Ow2GibiLSdloMLqKIaoQc30T/dN1HLf9s4DtAjCFTNo5 NQZe3G+pU5KnenVadFqWiOOtNpmUVBRvGBsllGB2kknA+b9Gdf/fEL4R9he6jIv7 U/NQ9PYi2QupgeXbPQIDAQAB"
#data={"x":"Hello yygy uvy  vai"}
#data="Gugh hvu h uth hvhy yuy"
#char="0"
#level=65
#token=obj.getTokenOfHash(data,char,level)
#signature=obj.signData(privateKey,data)
#print(obj.signData(privateKey,data))
#print(signature)
#signature=""
#print(obj.verifyData(publicKey,data,signature))
#print(obj.privateKeyToPublicKey(privateKey))
#print(token)
#print(obj.verifyTokenOfHash(data,token,char,level))