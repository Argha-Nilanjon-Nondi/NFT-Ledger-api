from lib.Validation import Validation
from flask import Flask,request,jsonify
from flask_cors import CORS
from lib.User import User
from lib.NFT import NFT
from lib.SecretCrypto import Cryptography
app=Flask(__name__)
CORS(app)
app.debug=True
app.host="0.0.0.0"
validated=Validation()

@app.route("/api/verify/user")
def verify_user_chain():
	objUser=User()
	data={}
	data["message"]="Verify the chain of user"
	data["code"]="200"
	data["data"]={"status":objUser.verify()}
	return data

@app.route("/api/profile/seller",methods=["POST"])
def profile_seller():
	data={}
	json_data = request.json;

	if (json_data == None):
		data["code"] = "406"
		data["message"] = "json data is not found"
		return data

	if (validated.checkJsonData(json_data, "public_key") == False):
		data["code"] = "406"
		data["message"] = "json data is not valid"
		return data

	publicKey=json_data["public_key"]
	
	if (validated.isPublicKeyExist(publicKey) == False):
		data["code"] = "404"
		data["message"] = "public key is not in the ledger"
		return data

	objNFT=NFT()
	data["message"]="profile of an user as seller"
	data["code"]="200"
	data["data"]={"as_seller":objNFT.detail_as_seller(publicKey=publicKey)}
	return data

@app.route("/api/profile/buyer",methods=["POST"])
def profile_buyer():
	data={}
	json_data = request.json;

	if (json_data == None):
		data["code"] = "406"
		data["message"] = "json data is not found"
		return data

	if (validated.checkJsonData(json_data, "public_key") == False):
		data["code"] = "406"
		data["message"] = "json data is not valid"
		return data

	publicKey=json_data["public_key"]

	if(validated.isPublicKeyExist(publicKey) == False):
		data["code"] = "404"
		data["message"] = "public key is not in the ledger"
		return data

	data["message"]="profile of an user as buyer"
	data["code"]="200"
	objNFT = NFT()
	data["data"]={"as_buyer":objNFT.detail_as_buyer(publicKey=publicKey)}
	return data

@app.route("/api/verify/nft")
def verify_nft_chain():
	objNFT=NFT()
	data={}
	data["message"]="Verify the chain of NFT"
	data["code"]="200"
	data["data"]={"status":objNFT.verify()}
	return data

@app.route("/api/verify/signature",methods=["POST"])
def verify_signature():
	data={}
	json_data = request.json;
	objNFT=NFT()
	if (json_data == None):
		data["code"] = "406"
		data["message"] = "json data is not found"
		return data
	if (validated.checkJsonData(json_data,"seller_public_key","signature")==False):
		data["code"] = "406"
		data["message"] = "json data is not valid"
		return data

	sellerPublicKey=json_data["seller_public_key"]
	signature=json_data["signature"]

	if (validated.isPublicKeyExist(sellerPublicKey) == False):
		data["code"]="404"
		data["message"]="seller public key for the private key is not in the ledger"
		return data

	if (validated.isSignatureExist(signature) == False):
		data["code"] = "404"
		data["message"] = "signature is not in the ledger"
		return data

	objNFT = NFT()
	data["code"]="200"
	data["message"]="verification of a signature"
	data["data"]={"status":objNFT.check_signature(sellerPublicKey=sellerPublicKey,signature=signature)}
	return data


@app.route("/api/add/user",methods=["POST"])
def add_user():
	data={}
	json_data = request.json;
	if (json_data == None):
		data["code"] = "406"
		data["message"] = "json data is not found"
		return data
	if (validated.checkJsonData(json_data,"username","nid","description")==False):
		data["code"] = "406"
		data["message"] = "json data is not valid"
		return data
	objUser = User()
	data["code"]="201"
	data["message"]="user is created"
	data["data"]=objUser.add(name=json_data["username"],nId=json_data["nid"],description=json_data["description"],level=3,char="0")
	return data


@app.route("/api/add/nft",methods=["POST"])
def add_nft():
	data={}
	json_data = request.json;
	if (json_data == None):
		data["code"] = "406"
		data["message"] = "json data is not found"
		return data
	if (validated.checkJsonData(json_data,"private_key","nft","file_location")==False):
		data["code"] = "406"
		data["message"] = "json data is not valid"
		return data

	privateKey=json_data["private_key"]
	nft=json_data["nft"]
	fileLocation=json_data["file_location"]

	obj = Cryptography()
	try:
		publicKey = obj.privateKeyToPublicKey(privateKey)
	except:
		data["code"]="400"
		data["message"]="private key is not valid"
		return data

	if (validated.isPublicKeyExist(publicKey) == False):
		data["code"]="404"
		data["message"]="public key for the private key is not in the ledger"
		return data

	if (validated.isNFTExist(nft) == True):
		data["code"]="404"
		data["message"]="NFT is already in the ledger"
		return data


	objNFT = NFT()
	data["code"]="201"
	data["message"]="NFT is added"
	data["data"]={"signature":objNFT.add_nft(privateKey=privateKey,nft=nft,fileLocation=fileLocation,level=3,char="0")}
	return data


@app.route("/api/transfer/nft",methods=["POST"])
def transfer_nft():
	data={}
	json_data = request.json;
	objNFT=NFT()
	if (json_data == None):
		data["code"] = "406"
		data["message"] = "json data is not found"
		return data
	if (validated.checkJsonData(json_data,"seller_private_key","buyer_public_key","nft")==False):
		data["code"] = "406"
		data["message"] = "json data is not valid"
		return data

	sellerPrivateKey=json_data["seller_private_key"]
	buyerPublicKey=json_data["buyer_public_key"]
	nft=json_data["nft"]

	obj = Cryptography()
	try:
		sellerPublicKey = obj.privateKeyToPublicKey(sellerPrivateKey)
	except:
		data["code"]="400"
		data["message"]="seller private key is not valid"
		return data

	if (validated.isPublicKeyExist(sellerPublicKey) == False):
		data["code"]="404"
		data["message"]="seller public key for the private key is not in the ledger"
		return data

	if (validated.isPublicKeyExist(buyerPublicKey) == False):
		data["code"]="404"
		data["message"]="buyer public key for the private key is not in the ledger"
		return data

	if (validated.isNFTExist(nft) == False):
		data["code"] = "404"
		data["message"] = "NFT is not in the ledger"
		return data

	if (sellerPublicKey == buyerPublicKey):
		data["code"] = "403"
		data["message"] = "you have the ownership already"
		return data

	owner_data = objNFT.findOwner(nft=nft)[0]
	owner = owner_data["buyer_public_key"]

	if (sellerPublicKey != owner):
		data["code"] = "401"
		data["message"] = "you do not have the ownership"
		return data

	objNFT = NFT()
	data["code"]="202"
	data["message"]="ownership of the NFT has been changed"
	data["data"]={"signature":objNFT.transfer_nft(sellerPrivateKey=sellerPrivateKey,buyerPublicKey=buyerPublicKey,nft=nft)}
	return data

@app.route("/api/detail/nft",methods=["POST"])
def detail_nft():
	data={}
	json_data = request.json;
	objNFT=NFT()
	if (json_data == None):
		data["code"] = "406"
		data["message"] = "json data is not found"
		return data
	if (validated.checkJsonData(json_data,"nft")==False):
		data["code"] = "406"
		data["message"] = "json data is not valid"
		return data

	nft=json_data["nft"]

	if (validated.isNFTExist(nft) == False):
		data["code"] = "404"
		data["message"] = "NFT is not in the ledger"
		return data

	nft_data = objNFT.findOwner(nft=nft)[0]

	objNFT = NFT()
	data["code"]="202"
	data["message"]="detail of NFT has been retrieved"
	data["data"]=nft_data
	return data

if __name__=="__main__":
	app.run()