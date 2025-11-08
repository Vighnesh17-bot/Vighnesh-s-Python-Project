import pandas as pd
import csv

print('''         Welcome to the Report Card Management System.         ''')
print('''          Please enter your login credentials          ''')

flag = True
l1 = []

# Step 1: Load database
with open('subdatabase.csv', 'r', newline='') as file:
    read = csv.reader(file)
    for rec in read:
        l1.append(rec)

# Step 2: Take login input and write to names.txt
login = input('Enter your username : ')
with open('names.txt', 'w') as file2:
    file2.write(login.strip())

pwd = input('Enter your password : ')

# Step 3: Verify login
flag = any(login in a for a in l1)

if login.lower() == 'teacher' and pwd.lower() == 'tpass':
    import teacher
    teacher.tlogin()
    print("""         Welcome to the teacher's page          """)

elif flag and pwd.lower() == 'spass':
    print("""         Welcome to the student's page           """)
    import student
    student.stulogin()

else:
    print('Invalid username/password. Please try again')
