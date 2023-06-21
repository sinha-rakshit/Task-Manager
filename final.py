import mysql.connector as db

mydb = db.connect(host="localhost", user="root", passwd="Qwerty@123", database="test")

mycursor = mydb.cursor()

choice = int(input("Enter your choice:"))

if choice == 1:
    userID = input("Enter Your UserID(Eg. rak123):")
    name = input("Enter Your Name:")
    Task = input("Enter the Task:")
    DeadLine = input("Enter the DeadLine:")
    sqlFormula = (
        "INSERT INTO Task_Manager(userID,NAME,TASK,DEADLINE) VALUES (%s,%s,%s,%s)"
    )
    sqlValues = (userID, name, Task, DeadLine)
    mycursor.execute(sqlFormula, sqlValues)
    mydb.commit()
