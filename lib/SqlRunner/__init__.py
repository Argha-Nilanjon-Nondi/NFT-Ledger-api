import sqlite3


class SqlRunner:
	def __init__(self,dbname):
		self.dbname=dbname
		self.connection = sqlite3.connect(self.dbname)
		self.cursor = self.connection.cursor()
		
	def run(self):
		self.cursor.execute(self.sql)
		self.connection.commit()
		record = self.cursor.fetchall()
		return record
		
	def close(self):
		self.cursor.close()
		self.connection.close()