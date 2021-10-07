#from lib.Writer import Writer
from lib.Book import Book

#objWriter=Writer()
#objAddWriter.add("","","","")
#print(objWriter.verify())
#print(objWriter.add(name="Argha Nilanjon Nondu",nId="12992749084",description="New member",level=3,char="0"))
privateKey="""
MIICXQIBAAKBgQC1hHA5JgDbNR7JRs5nkxL3DmL5vBZ9N8LTRiCRI+mNfOxXpxFm\n+adAyNDiiqH3XdiPMEKPntXja+TNlv64vhaG5fT/fZcOIOQYKJdEH7rJikY8ITp7\nrzFeVJMIc0tvoFzQb/mIB4XTCa78nSFyC7CyvaSRa+U0W7qemS+3Bn93BwIDAQAB\nAoGANgUkIN3eg15buysHYmuyyTPO4OPJDZr6sEW+i3NUnnb/H1bpJuxFilI5WDJJ\n4YRcXsDODlAG95e0kDrPs8teiGT37ao/Qj7LRtbhVPksJ2eOPdSTgg6161UEkrNZ\neljIxJkopX0g8fAq0zRkprgDu6Kxq6Eby696DJqG+RI0mgECQQC2wY92lcCtbOni\nLcT7WW9/2bh9zJ4sG4Vd0F5rYLDi7oN7Q+OsXLjvqFR9Ol7Xg1U2Xm8jZQVzckE5\nNG+k4wBXAkEA/kPIn00pWu1XaIlDJuK1jjwkQffA6/wYPioYz69XzmaQjaG1gD9g\nBRFSqVrai50Ks2k6MArUqncJu0nGUNdQ0QJBAKsuPnyq5GENJT2P9XQhX4j3nBFp\nObbCyHcJF4eod8b39fvdqUHnT+pbV1g89l0TTRux9JPIqgRqvqEgdnqRjd0CQQCJ\nCwnH6rPegUv6WPkrrUfD2OCF+b4usxpx7wieb9h4s8k3vS/xZrcfJB4Uj5Z5Z3RM\nDOxC1qOXGT/ShUnxaovxAkBct1A3phG0jE9gRO04taLiLMAteAOeRHAbD3cCaMGo\nNk7FZsz/0/6GHoyGEwcmdE3LagVBKmj7dkqffRQDwcVv
"""


objBook=Book()
print(objBook.check_signature())