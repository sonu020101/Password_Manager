import finder
import adder
import updater
import deleter
import displayer
import getpass
import sys
import key_manager
import os
from easygui import passwordbox


def password_validator(password):
    _PASSWORDMAIN = "Password" #change root password
    if password == _PASSWORDMAIN:
        return "Access granted"
    return "Dennied!!"



if __name__ == '__main__':
    ft=int(input("Is this your first time using program?\n"
                 "1. Yes \n"
                 "2. No \n"))
    if ft==1:
        key_manager.genwrite_key()


    while True:
        root_pass = passwordbox("Enter root password: ")
        # root_pass="Sonubitu@24"
        check = password_validator(root_pass)
        if check == "Access granted":
            print(check)
            path=input("Enter path of key file: ")
            if os.path.exists(path):
                while True:

                    x = int(input("Enter the choice: \n"
                                  "1. Check for password \n"
                                  "2. Add a new password \n"
                                  "3. Update password \n"
                                  "4. Delete password\n"
                                  "5. Display all passwords \n"
                                  "6. Exit\n"))
                    if x == 1:
                        while True:
                            choice = int(input("1. Find using username \n"
                                               "2. Find using website \n"
                                               "3. Go back previous menu \n"
                                               "4. Exit\n"))
                            if choice == 1:
                                flag = False
                                username = input("Please enter username of the site you want to access: ")
                                finder.finder_username(username,path)
                                break

                            elif choice == 2:
                                flag = False
                                website = input("Enter name of the website: ")
                                finder.finder_website(website,path)
                                break

                            elif choice == 3:
                                break

                            elif choice == 4:
                                sys.exit()

                            else:
                                print("Invalid input!!")
                    elif x == 2:
                        while True:
                            choice = int(input("1. Confirm adding new password \n"
                                               "2. Return back to previous menu\n"
                                               "3. Exit\n"))
                            if choice == 1:
                                adder.add_new(path)
                                break

                            elif choice == 2:
                                break

                            elif choice == 3:
                                sys.exit()

                            else:
                                print("Invalid input!!")

                    elif x == 3:
                        while True:
                            choice = int(input("1. Update using username: \n"
                                               "2. Update using website name: \n"
                                               "3. Return to previous menu \n"
                                               "4. Exit\n"))
                            if choice == 1:
                                username = input("Enter username: ")
                                status = updater.password_update_username(username,path)
                                if status == "Done":
                                    print(f"Password updated for {username}")
                                    break
                                else:
                                    print(status)
                                    break

                            elif choice == 2:
                                website = input("Enter website: ")
                                status = updater.password_update_name(website,path)
                                if status == "Done":
                                    print(f"Password updated for {website}")
                                    break
                                else:
                                    print(status)
                                    break

                            elif choice == 3:
                                break

                            elif choice == 4:
                                sys.exit()

                            else:
                                print("Invalid input!!")

                    elif x == 4:
                        while True:
                            choice = int(input("1. Delete using username: \n"
                                               "2. Delete using website \n"
                                               "3. Return to previous menu \n"
                                               "4. Exit\n"))
                            if choice == 1:
                                flag = False
                                username = input("Enter username: ")
                                status = deleter.delete_username(username,path)
                                if status == "Done":
                                    print(f"Password deleted for {username}")
                                    break
                                else:
                                    print(status)
                                    break

                            elif choice == 2:
                                website = input("Enter website name: ")
                                status = deleter.delete_website(website,path)
                                if status == "Done":
                                    print(f"Password deleted for {website}")
                                    break
                                else:
                                    print(status)
                                    break

                    elif x == 5:
                        displayer.display(path)
                    elif x == 6:
                        print("Thank you!\n"
                              "Developed by twok020101!")
                        sys.exit()
                    else:
                        print("Invalid input!!")
            else:
                print("No key file found access denied!")

        else:
            print(check)
            x = int(input("Do you want to enter password again? \n"
                          "1. Yes \n"
                          "2. No\n"))
            flag = True
            while flag:
                if x == 1:
                    flag = False
                    continue
                elif x == 2:
                    flag = False
                    break
                else:
                    print("Invalid input!")
