import pymysql as db
import sys
sys.path.append('D:\Python\PYTHON PROGRAM\Project\Prospect Encore Analysis')
import Admin,Monitor

connection = db.connect('localhost','root','Sniper','prospect_encore_analysis')
cursor = connection.cursor()
query = 'select * from employee'
cursor.execute(query)
result = cursor.fetchall()
username = input("Enter username: ")
password = input("Enter password: ")

for row in result:
    if row[0] == username and row[1] == password: # verify username and password
        if row[-1] == 'activated':  # if account status is activated then only the user is allowed
            if row[2] == 'admin': # if the user is an admin the open the Admin Menu
                Admin.mainmenu(username) # passing the username for later use while changing own password 
                print('You Are Successfully Logged Out !') 
                break
            else:
                Monitor.mainmenu(username) # passing the username for later use while changing own password 
                print('You Are Successfully Logged Out !')
                break
        else:
            print("Your Account is not Activated !")
            break
else:
    print("Employee not exists!")

cursor.close()
connection.close()
