import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  #'user':"annak83",
  #'password':"datareppass"
)

cursor = db.cursor()

cursor.execute("create DATABASE datarepresentation")

db.close()
cursor.close()