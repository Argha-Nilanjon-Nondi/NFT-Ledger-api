from lib.Writer import Writer
from lib.Book import Book

objWriter=Writer()
objBook=Book()


print("Chain of writer verification status:",objWriter.verify())
print("Chain of book verification status:",objBook.verify())