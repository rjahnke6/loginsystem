import csv
#CREATE ACCOUNT FUNCTION
def create():
    firstn = input("What is your first name?\n")
    lastn = input("What is your last name?\n")
    dateofbirth = input("What is your date of birth (MM/DD/YYYY?\n")
    i = 1
    while i == 1:
        file = open("userandpass.txt", "r")
        user = input("What would you like your username to be?\n")
        password = input("What would you like your password to be?\n")
        for line in file:
            if line.strip() == user:
                print("Username taken! Try again!")
                user = input("What would you like your username to be?\n")
                password = input("What would you like your password to be?\n")
                file.seek(0)                
        i = 2
    line = [user, password, firstn, lastn, dateofbirth]
    csvfile = open("userinfo.csv", "a")
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(line)
    csvfile.close()
    file.close()
    file = open("userandpass.txt", "a")
    file.write(user + '\n')
    file.write(password + '\n')
    file.close()
    print('\n')

#LOGIN FUNCTION
def login():
    file = open("userandpass.txt", "r")
    user = input("Username:\n")
    password = input("Password:\n")
    for line in file:
        if line.strip() == user:
            break
    else:
        print("User not found")
        return None
    if password != file.readline().strip(): #read line after found username
        print("Wrong password!")
    else:
        print("Username and Password Correct!")
    file.close()

#FORGOT PASSWORD FUNCTION
def forgotpass():
    file = open("userandpass.txt", "r")
    user = input("Input your username:\n")
    adminkey = input("Input the admin key to retrieve your password:\n")
    for line in file:
        if line.strip() == user:
            if adminkey == '8945':
                print("Users password is:", file.readline())
                return None
    else:
        print("User not found.")

#ADMINTOOLS FUNCTION
def admintools():
    i = 1
    while i == 1:
        adminkeyinput = input("Input admin key:\n")
        if adminkeyinput == '8945':
            print('\n')
            csvfile = open("userinfo.csv", "r")
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                print(line)
            csvfile.close()
            print('\n')
            i = 2
        else:
            print("ADMIN KEY WRONG! TRY AGAIN!")
