
# NFT Ledger

In this project , I have implemented blockchain technology with python. Here the data can not be changed or modify.So the database file can be share with anyone. If the person changes the database , we can detect it very easily.
A user can add NFT and change it's ownership.

## Installation
Install python 3.6 or higher version.
And run this command
```bash
  pip install pycryptodome
```

  
## Documentation
### Add  an user

#### code
```python
from lib.User import User

objUser=User()
print(objUser.add(name="Rahul Hassan",nId="128646979",description="New member",level=4,char="0"))
```
#### if the level=3 and char="0" then the hash will start with 000.The time to add a new writer will depends on the level . If the level is increased , the time will be increased as well.

#### output
```json
{
   'private_key': '2d2d2d2d2d424547494e20525341205052d0a4d4949435851494241414b42675143764a57786177......', 
   'public_key': '2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494......'
}
```

#### Here public_key is saved on ledger.sqlite but the private_key is not saved on ledger.sqlite. A user must save it on their computer and they should not share it with anyone but public_key can be shared with anyone

### Verify the users chain
#### code
```python
from lib.User import User

objUser=User()
print(objUser.verify())
```
#### output 1
```boolean
True
```
#### If anybody does not modify the data of the table named 'Users' of 'Ledger.sqlite' 

#### output 2
```boolean
False
```
#### If anybody modifies the data of the table named 'Users' of 'Ledger.sqlite'



### Verify the nfts chain
#### code
```python
from lib.NFT import NFT

objNFT=NFT()
print(objNFT.verify())
```
#### output 1
```boolean
True
```
#### If anybody does not modify the data of the table named 'NFTs' of 'Ledger.sqlite' 

#### output 2
```boolean
False
```
#### If anybody modifies the data of the table named 'NFTs' of 'Ledger.sqlite'



### Add a new NFT
#### code
```python
from lib.NFT import NFT

objNFT=NFT()

privateKey="2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d....."
nft="603c12257afa281384267d9af9ea57299d3e9d5e30dc4c6ed6b339e188d7db0d"
fileLocation="""https://drive.google.com/file/d/1mMLCgAOTddto82KTevoWjHu6EzjdtsFP/view?usp=drivesdk"""
level=3
char="0"

objNFT.add_nft(privateKey=privateKey,nft=nft,fileLocation=fileLocation,level=level,char=char)
```
#### if the level=3 and char="0" then the hash will start with 000.The time to add a new writer will depends on the level . If the level is increased , the time will be increased as well.

#### output
```text
42ac0cfec6b20078d0adb665479ed13ac85e1620fae5c24114e89c4858b477504095ad9a71d112e5fddal....
```
#### It is a signature of the NFT . It can be verify by using public key.


### Details of a NFT
#### code
```python
from lib.NFT import NFT

nft="603c12257afa281384267d9af9ea57299d3e9d5e30dc4c6ed6b339e188d7db0d"

objNFT=NFT()
print(objNFT.findOwner(nft=nft))
```
#### output
```json
[
   {
      'owner':'2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413.........', 
      'seller_public_key':'2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047435.......', 
      'buyer_public_key':'2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d4130474353714753......', 
     'token': 1664, 
     'signature':'29f0e4a8a5a42efb4012d0738e8ba2baa389fcfa57f96.....', 
     'status': 'nft_added', 
      'level': 3, 
      'char': '0', 
      'file_location':'https://drive.google.com/file/d/1mMLCgAOTddto82KTevoWjHu6EzjdtsFP/view?usp=drivesdk'
    }
]
```
#### owner and buyer_public_key have same value.



### Check a signature
#### code
```python
from lib.NFT import NFT

objNFT=NFT()

sellerPublicKey="2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664....."

signature="42ac0cfec6b20078d0adb665479ed13ac85e1620fae5c24114e89c4858b477504095ad9a71d112e5fd....."

print(objNFT.check_signature(sellerPublicKey=sellerPublicKey,signature=signature))
```
#### output 1
```text
True
```
#### If the signature is assigned with public key
#### output 2
```text
False
```
#### If the signature is not assigned with public key



### Transfer a NFT's ownership
#### code
```python
from lib.NFT import NFT

objNFT=NFT()

sellerPrivateKey="2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d....'"

buyerPublicKey="2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047435....."

nft="603c12257afa281384267d9af9ea57299d3e9d5e30dc4c6ed6b339e188d7db0d"

print(obj.transfer_nft(sellerPrivateKey=sellerPrivateKey,buyerPublicKey=buyerPublicKey,nft=nft))
```
#### output
```text
42ac0cfec6b20078d0adb665479ed13ac85e1620fae5c24114e89c4858b477504095ad9a71d112e5fddafc3e2da8f0f5fa008cef3ad4aa4a30541d04502e5029c7dc17
```
#### It returns a signature , which can be verify by using the public key

## Built with

 - python
 - sql
 - sqlite
- blockchain
- cryptography

  
## Note
- If you open the 'Ledger.sqlite' , you can not find the private key . So the database is a public ledger and it can shared with anyone.

- The level argument indeicates the hash complexity . The level argument is an integer type and it has the range of 1 to 64.

- You can change the 'getHash(data=,num=)' function in 'SecretCrypto/__init__.py'  so that  the hacker can not guess how hashes are being generated.

- I said earlier that you can share the 'Ledger.sqlite' with anyone but I will suggest that do not share the python scripts.

- It is a example of basic NFT marketing.

- It has some validation

- You can use the pattern in other scenarios. Like storing hash of files .
  
## License
- You can use it for educational purpose
- You can not claim it
- You can not use it for commercial purpose without my permission

  