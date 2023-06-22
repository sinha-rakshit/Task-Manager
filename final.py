import mysql.connector as db

mydb = db.connect(host="localhost", user="root", passwd="Qwerty@123", database="test")

mycursor = mydb.cursor()

choice = int(input("Enter your choice:"))

if choice == 1:
    userID = input("Enter Your UserID(Eg. rak123):")
    name = input("Enter Your Name:")
    Task = input("Enter the Task:")
    DeadLine = input("Enter the DeadLine(Eg. YYYY-MM-DD):")
    sqlFormula = (
        "INSERT INTO Task_Manager(userID,NAME,TASK,DEADLINE) VALUES (%s,%s,%s,%s)"
    )
    sqlValues = (userID, name, Task, DeadLine)
    mycursor.execute(sqlFormula, sqlValues)
    mydb.commit()

elif choice == 2:
    userID = input("Enter Your USERID(Eg. rak123):")
    sqlFormula = "DELETE FROM Task_Manager WHERE userID =%s"
    sqlValues = (userID,)  # tuple cannot be created with a comma
    mycursor.execute(sqlFormula, sqlValues)
    mydb.commit()

elif choice == 3:
    choiceUpdate = int(input("Enter the choice:"))
    if choiceUpdate == 1:
        userID_old = input("Enter the userID(old):")
        userID_new = input("Enter the userID(new):")
        sqlFormula = "UPDATE Task_Manager SET userID=%s WHERE userID=%s"
        sqlValues = (userID_new, userID_old)
        mycursor.execute(sqlFormula, sqlValues)
        mydb.commit()

    elif choiceUpdate == 2:
        userID = input("Enter the userID:")
        name_old = input("Enter your name(old):")
        name_new = input("Enter your name(new):")
        sqlFormula = "UPDATE Task_Manager SET NAME=%s WHERE userID=%s AND NAME=%s"
        sqlValues = (name_new, userID, name_old)
        mycursor.execute(sqlFormula, sqlValues)
        mydb.commit()

    elif choiceUpdate == 3:
        userID = input("Enter the userID:")
        task_old = input("Enter your Task(old):")
        task_new = input("Enter your Task(new):")
        sqlFormula = "UPDATE Task_Manager SET TASK=%s WHERE userID=%s AND TASK=%s"
        sqlValues = (task_new, userID, task_old)
        mycursor.execute(sqlFormula, sqlValues)
        mydb.commit()

    elif choiceUpdate == 4:
        userID = input("Enter the userID:")
        Deadline_old = input("Enter your Deadline(old):")
        Deadline_new = input("Enter your Dealine(new):")
        sqlFormula = (
            "UPDATE Task_Manager SET DEADLINE=%s WHERE userID=%s AND DEADLINE=%s"
        )
        sqlValues = (Deadline_new, userID, Deadline_old)
        mycursor.execute(sqlFormula, sqlValues)
        mydb.commit()
