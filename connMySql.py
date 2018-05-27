import mysql.connector
class FlaskrDB:
	def __init__(self,config):
		self.configuration = config
	def __enter__(self):
		self.conn = mysql.connector.connect(**self.configuration)
		self.cursor = self.conn.cursor()
		return self.cursor
	def __exit__(self,val1,val2,val3):
		self.conn.commit()
		self.cursor.close()
		self.conn.close()