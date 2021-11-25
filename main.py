from student_management_system import display_record,add_new_student,search_student,update_student,delete_student,create_user,login_user

import platform, os


def check_user(cur,conn):
    print('''
    ## Welcome to Student Management System ##
    Enter 1: To login to system
    Enter 2: To register into
    Enter 3: To exit  \n''')
    try:
        user_option = int(input("Enter the option: "))
    except ValueError:
        exit("This is not the number")
    
    if(user_option == 1):
        
        if login_user(cur):
            main(cur,conn)
        else:
            print("Username or password incorrect")
            print("cannot login")
            check_user(cur,conn)


    elif(user_option == 2):
        print("Enter your information to register: ")
        create_user(cur, conn)
        check_user(cur,conn)

    elif(user_option == 3):
        print("BYE")
        quit()

    else:
        print("Cannot enter value greater than 3")
        quit()
    

def main(cur,conn):

    print("""
    ## Welcome to Student Management System ##
    Enter 1: To view student List
    Enter 2: To add new Student
    Enter 3: To search student
    Enter 4: To update student
    Enter 5: To delete student 
    Enter 6: To logout \n """)

    try:
        user_input = int(input("Please select an option "))

    except ValueError:
        exit("Thats not the number")
    else:
        print('\n')

    if(user_input == 1):
        print("List of student \n")
        cur.execute("SELECT * from student")
        records = cur.fetchall()
        display_record(records)

    elif(user_input == 2):
        print("Add new student")
        add_new_student(cur,conn)
        
    elif(user_input == 3):
        print("search student")
        search_student(cur)
        
    
    elif(user_input == 4):
        print("Update student")
        update_student(cur,conn)
        
    
    elif(user_input == 5):
        print("Delete student")
        delete_student(cur,conn)
    
    elif(user_input == 6):
        check_user(cur,conn)

    else:
        print("Invalid option selected")
        quit()

def runagain(cur,conn):
    runagain_i = input("Want to run again Y/n ")
    if runagain_i.lower() == 'y':
        if platform.system() == "Windows":
            print(os.system('cls')) 
        else:
            print(os.system('clear')) 
        main(cur,conn)
        runagain(cur,conn)

    else:
        print("Bye")
        quit()

