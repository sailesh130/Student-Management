from student_management_system import display_record,add_new_student,search_student,update_student,delete_student,stds
import platform,os
from teacher import Supervisor
def main():
    
    print("""
    ## Welcome to Student Management System ##
    Enter 1: To view student List
    Enter 2: To add new Student
    Enter 3: To search student
    Enter 4: To update student
    Enter 5: To delete student \n """)

    try:
        user_input = int(input("Please select an option "))

    except ValueError:
        exit("Thats not the number")
    else:
        print('\n')

    if(user_input == 1):
        print("List of student \n")
        display_record(stds)

    elif(user_input == 2):
        print("Add new student")
        add_new_student()
        
    elif(user_input == 3):
        print("search student")
        search_student()
        
    
    elif(user_input == 4):

        print("Update student")
        update_student()
        
    
    elif(user_input == 5):
        print("Delete student")
        delete_student()
        

    else:
        print("Invalid option selected")
        quit()

def runagain():
    runagain_i = input("Want to run again Y/n ")
    if runagain_i.lower() == 'y':
        if platform.system() == "Windows":
            print(os.system('cls')) 
        else:
            print(os.system('clear')) 
        main()
        runagain()

    else:
        print("Bye")
        quit()

main()
runagain()