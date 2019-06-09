#MODULE IMPORT
import functions

#MAIN MENU
i = 1
menuopts = [1,2,3,4,5]
while i == 1:
    print("1: Create an account")
    print("2: Login")
    print("3: Forgot Password")
    print("4: Quit Software")
    print("5: User's Info")
    try:
        menuoption = int(input("Which menu option would you like to chose?\n"))
        if menuoption == 1:
            functions.create()
        if menuoption == 2:
            functions.login()
        if menuoption == 3:
            functions.forgotpass()
        if menuoption == 4:
            print("TERMINATING PROGRAM")
            quit()
        if menuoption == 5:
            functions.admintools()
        if menuoption not in menuopts:
            print("That was not an option on the menu! TRY AGAIN!!\n")
    except ValueError:
        print("That was not an option on the menu! TRY AGAIN!\n")
