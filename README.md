
# NFT Ledger REST API

In this project , I have implemented blockchain technology with python. Here the data can not be changed or modify.So the database file can be share with anyone. If the person changes the database , we can detect it very easily.
A user can add NFT and change it's ownership. It is a rest api.

<br>
<br>


## Installation
Install python 3.6 or higher version.
And run this command
```bash
pip install pycryptodome==3.11.0
pip install flask==1.1.2
pip install flask-cors==3.0.10
```

<br>
<br>


## Knowledge
- [NFT](https://en.wikipedia.org/wiki/Non-fungible_token)
- [Blockchain](https://en.wikipedia.org/wiki/Blockchain)
- [Public and private key](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [Digital Signature](https://en.wikipedia.org/wiki/Digital_signature)
- [Hashing](https://en.wikipedia.org/wiki/Hash_function)
- [REST API](https://restfulapi.net/)

<br>
<br>

  
## API Reference

### Verify the chain of user
  
#### URL  
```http
GET http://localhost:5000/api/verify/user
```

#### Response
```json
{
    "code": 200,
    "data": {
        "status": true
    },
    "message": "Verify the chain of user"
}
```

<br />


### Verify the chain of NFT
  
#### URL  
```http
GET http://localhost:5000/api/verify/nft
```

#### Response
```json
{
    "code": 200,
    "data": {
        "status": true
    },
    "message": "Verify the chain of NFT"
}
```

<br />




### Add a user
  
#### URL  
```http
POST http://localhost:5000/api/add/user
```

#### Json Data
```json
{
    "username":"Karim Hassan",
    "description":"New memeber",
    "nid":"3246564543"
}
```

#### Response
```json
{
    "code": "201",
    "data": {
        "private_key": "2d2d2d2d2d424547494e20525341205052492d.....",
        "public_key": "2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2...."
    },
    "message": "user is created"
}
```

<br />



### Add a NFT
  
#### URL  
```http
POST http://localhost:5000/api/add/nft
```

#### Json Data
```json
{
    "private_key":"2d2d2d2d2d424547494e2052534163495047413d3d0a2d2d2d2d...",
    "nft":"a53c12257afa281384267d9af9ec57299d3e9d5e30dc4c6ed6b339e188d7db0a",
    "file_location":"https://drive.google.com/file/d/1mMLCgAOTddto82KTevoWjHu6EzjdtsFP/view?usp=drivesdk"
}
```

#### Response
```json
{
    "code": "201",
    "data": {
        "signature": "7ebaf58a02ce8955831a8e8f67b20bbab951f8d7e3b379048c3560b9e37b7920d735da97a4bc24304d10c1466660f1bc214be5b77b68c6c0a297a5b1654c6842ec6f806403a6c45d045246a30c2b49920e8539bccdeb7d5c638fd900fdee47e2916e3a4c4c1a8dd05c7e28ea7ed6ffd86b8218447b64e143a124751a2b3bd762"
    },
    "message": "NFT is added"
}
```

<br />



### Change the ownership of a NFT
  
#### URL  
```http
POST http://localhost:5000/api/transfer/nft
```

#### Json Data
```json
{
    "seller_private_key":"2d2d2d2d2d424547494e205253412050524956415445204b45592d2d2d2d2d0a4.......",
    "nft":"a53c12257afa281384267d9af9ec57299d3e9d5e30dc4c6ed6b339e188d7db0a",
    "buyer_public_key":"2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d413........"
}
```

#### Response
```json
{
    "code": "202",
    "data": {
        "signature": "543c6257c3c265e171783c5d1feb1038d909a0a319a34e05fc7b50aaa47a08fabe2bc13df833cdffd16cd....."
    },
    "message": "ownership of the NFT has been changed"
}
```

<br />



### Get details of a NFT
  
#### URL  
```http
POST http://localhost:5000/api/detail/nft
```

#### Json Data
```json
{
    "nft":"a53c12257afa281384267d9af9ec57299d3e9d5e30dc4c6ed6b339e188d7db0a"
}
```

#### Response
```json
{
    "code": "202",
    "data": {
        "buyer_public_key": "2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d4130.....",
        "file_location": "https://drive.google.com/file/d/1mMLCgAOTddto82KTevoWjHu6EzjdtsFP/view?usp=drivesdk",
        "owner": "2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d41304743537147534962.....",
        "seller_public_key": "2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4d4947664d41304743537147534.....",
        "signature": "543c6257c3c265e171783c5d1feb1038d909a0a319a34e05fc7b50aaa47a08fab.....",
        "status": "ownership_changed",
    },
    "message": "detail of NFT has been retrieved"
}
```

<br />



### Verify a signature
  
#### URL  
```http
POST http://localhost:5000/api/verify/signature
```

#### Json Data
```json
{
"seller_public_key": "2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a4.....",
"signature": "543c6257c3c265e171783c5d1feb1038d909a0a319a34e05fc7b50aaa47a08fabe2bc13df83....."
}
```

#### Response
```json
{
    "code": "200",
    "data": {
        "status": true
    },
    "message": "verification of a signature"
}
```

<br />




### Defails of a profile as seller
  
#### URL  
```http
POST http://localhost:5000/api/profile/seller
```

#### Json Data
```json
{
    "public_key":"2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a......"
}
```

#### Response
```json
{
    "code": "200",
    "data": {
        "as_seller": [
            {
                "buyer_public_key": "2d2d2d2d2d424547494e205055424c4943204b4559......",
                "event_date": "2021-10-14 08:59:55",
                "file_location": "https://images.unsplash.com/photo-1634148208442-651545......",
                "nft": "fe6c3ef3e77665d136d4f4d27eae5b5c2a97010807fef9ecfc0f6a4af6a8bf87",
                "signature": "19aa451f26186673df2799f84e74b76a1d7fd3cdf0a68db3028893565bc620258.......",
                "status": "nft_added"
            }
        ]
    },
    "message": "profile of an user as seller"
}
```

<br />



### Defails of a profile as buyer
  
#### URL  
```http
POST http://localhost:5000/api/profile/buyer
```

#### Json Data
```json
{
    "public_key":"2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2d2d0a......"
}
```

#### Response
```json
{
    "code": "200",
    "data": {
        "as_buyer": [
            {
                "event_date": "2021-10-14 08:59:55",
                "file_location": "https://images.unsplash.com/photo-1634148208442-651545....",
                "nft": "fe6c3ef3e77665d136d4f4d27eae5b5c2a97010807fef9ecfc0f6a4af6a8bf87",
                "seller_public_key": "2d2d2d2d2d424547494e205055424c4943204b45592d2d2d2......",
                "signature": "19aa451f26186673df2799f84e74b76a1d7fd3cdf0a68db3028893565b.......",
                "status": "nft_added"
            }
        ]
    },
    "message": "profile of an user as buyer"
}
```

<br />
<br>

## Built with

 - python
 - sql
 - sqlite
- blockchain
- cryptography

<br>
<br>

## Note
- If you open the 'Ledger.sqlite' , you can not find the private key . So the database is a public ledger and it can shared with anyone.

- The level argument indeicates the hash complexity . The level argument is an integer type and it has the range of 1 to 64.

- You can change the 'getHash(data=,num=)' function in 'SecretCrypto/__init__.py'  so that  the hacker can not guess how hashes are being generated.

- I said earlier that you can share the 'Ledger.sqlite' with anyone but I will suggest that do not share the python scripts.

- It is a example of basic NFT marketing.

- It has some validation

- You can use the pattern in other scenarios. Like storing hash of files .

<br>
  
## License
- You can use it for educational purpose
- You can not claim it
- You can not use it for commercial purpose without my permission

  