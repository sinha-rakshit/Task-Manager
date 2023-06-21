import mysql.connector as db

mydb = db.connect(host="localhost", user="root", passwd="Qwerty@123", database="test")

mycursor = mydb.cursor()

name = input("Enter your name:")
age = int(input("Enter your age:"))


# sqlFormula = "INSERT INTO student_test(name, age) VALUES (%s,%s)"
# studentInput = (name, age)
# mycursor.execute(sqlFormula, studentInput)
# mydb.commit()

sqlFormula = "UPDATE student_test SET NAME=%s WHERE AGE=%s"
values = (name, 10)
mycursor.execute(sqlFormula, values)
mydb.commit()
