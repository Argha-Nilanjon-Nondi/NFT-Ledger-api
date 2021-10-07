
# Story Blockchain

In this project , I have implemented blockchain technology with python. Here the data can not be changed or modify.So the database file can be share with anyone. If the person changes the database , we can detect it very easily.

## Installation
Install python 3.6 or higher version.
And run this command
```bash
  pip install pycryptodome
```

  
## Documentation
### Add a writer

#### code
```python
from lib.Writer import Writer

objWriter=Writer()
print(objWriter.add(name="Argha Nilanjon Nondi",nId="12992749084",description="New member",level=3,char="0"))
```
#### if the level=3 and char="0" then the hash will start with 000.The time to add a new writer will depends on the level . If the level is increased , the time will be increased as well.

#### output
```json
{
   "private_key": "2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d0a4d4949435851494241414b42675143764a57786177......", 
   "public_key": "2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d494......"
}
```

#### Here public_key is saved on ledger.sqlite but the private_key is not saved on ledger.sqlite. A user must save it on their computer and they should not share it with anyone but public_key can be shared with anyone

### Verify the Writers chain
#### code
```python
from lib.Writer import Writer

objWriter=Writer()
print(objWriter.verify())
```
#### output 1
```boolean
True
```
#### If anybody does not modify the data of the table named 'Writers' of 'Ledger.sqlite' 

#### output 2
```boolean
False
```
#### If anybody modifies the data of the table named 'Writers' of 'Ledger.sqlite'



### Add a story
#### code
```python
from lib.Story import Story

privateKey="""2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d..."""
objStory=Story()
print(objStory.add(privateKey=privateKey,storyName="Doctor Sleep",storyDescription="A horror thriller book",level=3,char="0"))
```
#### if the level=3 and char="0" then the hash will start with 000.The time to add a new writer will depends on the level . If the level is increased , the time will be increased as well. Here hash is not the signature.
#### output
  ```text
7011f882ad281ec19f300a4c9017961338f48ecacdcbb4b370dda34eaae5e9601......
```
####  It is the signature of a story and it can be shared with anyone.



### Verify the Stories chain
#### code
```python
from lib.Story import Story

objWriter=Story()
print(objWriter.verify())
```
#### output 1
```boolean
True
```
#### If anybody does not modify the data of the table named 'Stories' of 'Ledger.sqlite' 

#### output 2
```boolean
False
```
#### If anybody modifies the data of the table named 'Stories' of 'Ledger.sqlite

### Verify a signature
#### code
```python
from lib.Story import Story

signature="5f9dc207c0577846a40cf5c4fecb4b781d7980482e4b6fa62cfb63514be01d581535d59da29a....."

publicKey="""2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413047......."""

objStory=Story()
print(objStory.check_signature(signature=signature,publicKey=publicKey))
```
#### output 1
```boolean
True
```
#### If anybody does not modify the data of the table named 'Stories' of 'Ledger.sqlite'  or the signature is connected to public key
#### output 2
```boolean
False
```
 If anybody modifies the data of the table named 'Stories' of 'Ledger.sqlite or the signature is not connected to public key

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

- You can use the pattern in other scenarios. Like storing hash of files .
  
## License
- You can use it for educational purpose
- You can not claim it
- You can not use it for commercial purpose without my permission

  