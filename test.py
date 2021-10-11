import hashlib

file=open("img.png","rb")
content=file.read()
print(hashlib.sha256(content).hexdigest())
file.close()