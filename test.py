import mysql.connector as db

mydb = db.connect(host="localhost", user="root", passwd="Qwerty@123")

print(mydb)
