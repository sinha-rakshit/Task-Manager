import mysql.connector as db

mydb = db.connect(host="localhost", user="root", passwd="Qwerty@123", database="test")

# working table is student_test
mycursor = mydb.cursor()


# To enter DATA:

sqlFormula = "INSERT INTO student_test (name, age) VALUES (%s,%s)"
studentsInput = [("Rakshit", 18), ("Rahul", 8), ("Harsh", 10)]
mycursor.executemany(sqlFormula, studentsInput)
mydb.commit()

# To check DATA(of all rows):

# mycursor.execute("SELECT * from student_test")
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)

# To check DATA(with WHERE)

# sqlFormula = "SELECT * from student_test WHERE age=10"
# mycursor.execute(sqlFormula)
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)

# To Update DATA
# sqlFormula = "UPDATE student_test SET NAME='Sandihya' WHERE AGE=10"
# mycursor.execute(sqlFormula)
# mydb.commit()
