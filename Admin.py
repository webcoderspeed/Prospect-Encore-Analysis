import pymysql as db
import os 
connection = db.connect('localhost','root','Sniper','prospect_encore_analysis')
cursor = connection.cursor()

def create_user_account():
    def create_admin_account():
        username = input('Enter Username:')
        userpass = input('Enter Password: ')
        fullname = input('Enter Fullname: ')
        phone = input('Enter Phonenumber: ')
        email = input('Enter Email: ')
        status = input('Enter Account Status: ')
        query = f"""insert into employee values('{username}','{userpass}','admin','{fullname}','{phone}','{email}','{status}')"""
        cursor.execute(query)
        connection.commit()
        
    def create_monitor_account():
        username = input('Enter Username:')
        userpass = input('Enter Password: ')
        fullname = input('Enter Fullname: ')
        phone = input('Enter Phonenumber: ')
        email = input('Enter Email: ')
        status = input('Enter Account Status: ')
        query = f"""insert into employee values('{username}','{userpass}','monitor','{fullname}','{phone}','{email}','{status}')"""
        cursor.execute(query)
        connection.commit()

    while True:
        choice = int(input("""
        1) Create Admin Account:
        2) Create Monitor Account: 
        3) Exit
        Enter your choice:  """))
        if choice == 1:
            create_admin_account()
        if choice == 2:
            create_monitor_account()
        elif choice == 3:
            break
        else:
            print("Invalid Choice")
        os.system("pause")

def view_all_employees():
    query = "Select * from employee"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

def view_all_propects():
    query = "Select * from prospect"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

def change_password(username):
    def self_password(username):
        userpass = input('Enter new userpass: ')
        query = f"""update employee set userPass = '{userpass}' where userName ='{username}' """
        cursor.execute(query)
        connection.commit()
    def others_password():
        username = input('Enter Username: ')
        userpass = input('Enter new userpass: ')
        query = f"""update employee set userPass = '{userpass}' where userName ='{username}' """
        cursor.execute(query)
        connection.commit()
    while True:
        choice = int(input("""
        1) Change Own Password
        2) Change Other Password
        3) Exit
        Enter your choice:  """))
        if choice == 1:
            self_password(username)
        if choice == 2:
            others_password()
        elif choice == 3:
            break
        else:
            print("Invalid Choice...")
        os.system("pause")
        

def search_prospect():
    def search_by_priority():
        priority = input('Enter Priority: ')
        query = f"""select * from prospect where priority = '{priority}'"""
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    def search_by_prospid():
        prospid = input('Enter Propect Id: ')
        query =f"""Select * from prospect where prospId = {prospid}"""
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
    while True:
        choice = int(input("""
        1) Search By Priority
        2) Search By ProspId
        3) Exit
        Enter your choice:  """))
        if choice == 1:
            search_by_priority()
        elif choice == 2:
            search_by_prospid()
        elif choice == 3:
            break
        else:
            print("Invalid Choice...")
        os.system("pause")

def set_account_status():
    username = input('Enter Username: ')
    status = input('Enter Status: ')
    query = f"""update employee set status = '{status}' where userName ='{username}' """
    cursor.execute(query)
    connection.commit()        

def mainmenu(username):
    while True:
        os.system('cls')
        choice = int(input("""-------------------  MAIN MENU   ----------------------
        1) Create User Account: 
        2) View All Users/Emloyees
        3) View All Prospects
        4) Change Password
        5) Search By Prospect
        6) Activate/ Deactivate Account
        7) SignOut
        Enter your choice: """))

        if choice == 1:
            create_user_account()
        elif choice == 2:
            view_all_employees()
        elif  choice == 3:
            view_all_propects()
        elif choice == 4:
            change_password(username)
        elif choice == 5:
            search_prospect()
        elif choice == 6:
            set_account_status()
        elif choice == 7:
            break    
        else:
            print("Invalid Choice")
        os.system("pause")
    cursor.close()
    connection.close()



