import pymysql as db
import os 
connection = db.connect('localhost','root','Sniper','prospect_encore_analysis')
cursor = connection.cursor()
import Admin

def add_new_prospect():
    propsId = input('Enter PropsId:')
    prospName = input('Enter ProspName:')
    prospPhone = input('Enter Phone:')
    prospAddress = input('Enter ProspAddress:')
    interestedModel = input('Enter Instrested Model:')
    intrestedColor = input('Enter Intrested Color:')
    dateOfVisit = input('Enter Date of Visit:')
    priority = input('Enter Priority: ')
    query = f"""insert into prospect values(
        {propsId},'{prospName}','{prospPhone}','{prospAddress}','{interestedModel}',
        '{intrestedColor}','{dateOfVisit}','{priority}'
    )
    """
    cursor.execute(query)
    connection.commit()

def change_password(username):
        userpass = input('Enter new userpass: ')
        query = f"""update employee set userPass = '{userpass}' where userName ='{username}' """
        cursor.execute(query)
        connection.commit()

def update_prospect():
    def update_name():
        prospId = input("Enter ProspId: ")
        prospName = input('Enter ProspName:')
        query = f"""update prospect set prospName = '{prospName}' where prospId = {prospId}"""
        cursor.execute(query)
        connection.commit()
    def update_Phone():
        prospId = input("Enter ProspId: ")
        prospPhone = input('Enter ProspPhone:')
        query = f"""update prospect set prospPhone = '{prospPhone}' where prospId = {prospId}"""
        cursor.execute(query)
        connection.commit()
    def update_Address():
        prospId = input("Enter ProspId: ")
        prospAddress = input('Enter ProspAddress:')
        query = f"""update prospect set prospAddress = '{prospAddress}' where prospId = {prospId}"""
        cursor.execute(query)
        connection.commit()
    def update_model():
        prospId = input("Enter ProspId: ")
        instrestedModel = input('Enter InstrestedModel:')
        query = f"""update prospect set intrestedmodel = '{instrestedModel}' where prospId = {prospId}"""
        cursor.execute(query)
        connection.commit()
    def update_color():
        prospId = input("Enter ProspId: ")
        instrestedColor = input('Enter InstrestedColor:')
        query = f"""update prospect set intrestedColor = '{instrestedColor}' where prospId = {prospId}"""
        cursor.execute(query)
        connection.commit()
    def update_date_of_visit():
        prospId = input('Enter ProspId:')
        dateOfVisit = input('Enter Date Of Visit:')
        query = f"""update prospect set intrestedColor = '{dateOfVisit}' where prospId = {prospId}"""
        cursor.execute(query)
        connection.commit()
    def update_priority():
        prospId = input('Enter ProspId:')
        priority = input('Enter Priority:')
        query = f"""update prospect set intrestedColor = '{priority}' where prospId = {prospId}"""
        cursor.execute(query)
        connection.commit()
    while True:
        os.system('cls')
        choice = int(input("""-------------------  MAIN MENU   ----------------------
        1) Update Name
        2) Update Phone
        3) Update Address
        4) Update Model
        5) Update Color
        6) Update Date Of Visit
        7) Update Priority
        8) Exit
        Enter your choice: """))

        if choice == 1:
            update_name()
        elif choice == 2:
            update_Phone()
        elif choice == 3:
            update_Address()
        elif choice == 4:
            update_model()
        elif choice == 5:
            update_color()
        elif choice == 6:
            update_date_of_visit()
        elif choice == 7:
            update_priority()
        elif choice == 8:
            break
        else:
            print("Invalid Choice")
        os.system("pause")

def mainmenu(username):
    while True:
        os.system('cls')
        choice = int(input("""-------------------  MAIN MENU   ----------------------
        1) Add New Prospect
        2) View All Prospect
        3) Update Prospect
        4) Change Password
        5) Search By Prospect
        6) SignOut
        Enter your choice: 
        """))

        if choice == 1:
            add_new_prospect() 
        elif choice == 2:
            Admin.view_all_propects()
        elif choice == 3:
            update_prospect()
        elif choice == 4:
            change_password(username)
        elif choice == 5:
            Admin.search_prospect()
        elif choice == 6:
            break    
        else:
            print("Invalid Choice")
        os.system("pause")
    cursor.close()
    connection.close()
