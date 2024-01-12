import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #'user':"annak83",
  #'password':"datareppass"
  database="datarepresentation"
)

cursor = db.cursor()
sql="CREATE TABLE data (year VARCHAR(250), sex VARCHAR(250), age_group VARCHAR(250), average_height float)"

cursor.execute(sql)

db.close()
cursor.close()