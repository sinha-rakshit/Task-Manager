import mysql.connector as db

mydb = db.connect(host="localhost", user="root", passwd="Qwerty@123", database="test")

mycursor = mydb.cursor()

print("WELCOME TO THE TASK MANAGER:")
print("PRESS 1 IF NEW USER:")
print("PRESS 2 IF OLD USER AND WANT TO ADD TASK:")
print("PRESS 3 TO DELETE USER:")
print("PRESS 4 TO DELETE TASK:")
print("PRESS 5 TO UPDATE:")
print("PRESS 6 TO SEARCH TASKS:")

choice = int(input("Enter your choice:"))

if choice == 1:  # to enter your User Info
    userID = input("Enter Your UserID(Eg. rak123):")
    name = input("Enter Your Name:")
    Date_of_birth = input("Enter your Date of Birth(Eg. YYYY-MM-DD):")
    sqlFormula = "INSERT INTO User_Info(userID,NAME,Date_of_Birth) VALUES (%s,%s,%s)"
    sqlValues = (userID, name, Date_of_birth)
    mycursor.execute(sqlFormula, sqlValues)
    mydb.commit()

elif choice == 2:
    task_id = input("Enter Your TaskID(Eg. task_type):")
    user_ID = input("Enter Your USERID(Eg. rak123):")
    Task = input("Enter your Task:")
    Deadline = input("Enter the Deadline:")
    sqlFormula = "INSERT INTO Task(task_id,user_ID,Task,Deadline) VALUES (%s,%s,%s,%s)"
    sqlValues = (task_id, user_ID, Task, Deadline)
    mycursor.execute(sqlFormula, sqlValues)
    mydb.commit()


elif choice == 3:
    userID = input("Enter Your USERID(Eg. rak123):")
    sqlFormula = "DELETE FROM User_Info WHERE userID =%s"
    sqlFormula2 = "DELETE FROM Task WHERE user_ID =%s"
    sqlValues = (userID,)  # tuple cannot be created with a comma
    mycursor.execute(sqlFormula, sqlValues)
    mycursor.execute(sqlFormula2, sqlValues)
    mydb.commit()

elif choice == 4:
    task_id = input("Enter Your Task ID:")
    sqlFormula = "DELETE FROM Task WHERE task_id=%s"
    sqlValues = (task_id,)
    mycursor.execute(sqlFormula, sqlValues)
    mydb.commit()

elif choice == 5:
    print("PRESS 1 TO UPDATE USERID:")
    print("PRESS 2 TO UPDATE NAME:")
    print("PRESS 3 TO UPDATE TASK:")
    print("PRESS 4 TO UPDATE DEADLINE:")
    choiceUpdate = int(input("Enter the choice:"))
    if choiceUpdate == 1:
        userID_old = input("Enter the userID(old):")
        userID_new = input("Enter the userID(new):")
        sqlFormula = "UPDATE User_Info SET userID=%s WHERE userID=%s"
        sqlFormula2 = "UPDATE Task SET user_ID=%s WHERE user_ID=%s"
        sqlValues = (userID_new, userID_old)
        mycursor.execute(sqlFormula, sqlValues)
        mycursor.execute(sqlFormula2, sqlValues)
        mydb.commit()

    elif choiceUpdate == 2:
        userID = input("Enter the userID:")
        name_old = input("Enter your name(old):")
        name_new = input("Enter your name(new):")
        sqlFormula = "UPDATE User_Info SET NAME=%s WHERE userID=%s AND NAME=%s"
        sqlValues = (name_new, userID, name_old)
        mycursor.execute(sqlFormula, sqlValues)
        mydb.commit()

    elif choiceUpdate == 3:
        Task_ID = input("Enter the TaskID:")
        task_old = input("Enter your Task(old):")
        task_new = input("Enter your Task(new):")
        sqlFormula = "UPDATE Task SET TASK=%s WHERE task_id=%s AND TASK=%s"
        sqlValues = (task_new, Task_ID, task_old)
        mycursor.execute(sqlFormula, sqlValues)
        mydb.commit()

    elif choiceUpdate == 4:
        Task_ID = input("Enter the TaskID:")
        Deadline_old = input("Enter your Deadline(old):")
        Deadline_new = input("Enter your Dealine(new):")
        sqlFormula = (
            "UPDATE Task_Manager SET DEADLINE=%s WHERE task_id=%s AND DEADLINE=%s"
        )
        sqlValues = (Deadline_new, Task_ID, Deadline_old)
        mycursor.execute(sqlFormula, sqlValues)
        mydb.commit()

elif choice == 6:
    userID = input("Enter the User ID:")
    sqlFormula = "SELECT User_Info.userID, User_Info.NAME, Task.Task, Task.Deadline FROM User_Info INNER JOIN Task ON User_Info.userID = Task.User_ID WHERE User_Info.userID = %s"
    sqlValues = (userID,)
    mycursor.execute(sqlFormula, sqlValues)
    result = mycursor.fetchall()

    if len(result) == 0:
        print("No matching records found.")

    else:
        print("ID   NAME   TASK     Deadline")
        for db in result:
            print(db[0], "   ", db[1], "   ", db[2], "     ", db[3])
