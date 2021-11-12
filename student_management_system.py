import os
import platform
global stds
stds = []
class Student():
    def __init__(self,name,age,roll_no,grade,address):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.grade = grade
        self.address = address
        
    def __str__(self):
        return f"""
        Name:{self.name.capitalize()}
        Age:{self.age} 
        Roll no:{self.roll_no}
        Grade: {self.grade}
        Address: {self.address}"""

    def __del__(self):
        print (f"deleted {self.name} record.")

def search_record(name):
    if name not in [obj.name for obj in stds]:
        return True

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
        if len(stds)==0:
            
            print("No student in the record\n")
        else:
            for i in stds:
                print("=> ",i)

    elif(user_input == 2):
        print("Add new student")
        name = input("Enter name: ")
        age = int(input("Enter age of student: "))
        roll_no = input("Enter roll no of student: ")
        grade = input("Enter grade of student: ")
        address = input("Enter address of student: ")

        obj = Student(name,age,roll_no,grade,address)
        print("Added information:")
        print(obj,"\n")
        stds.append(obj)
        

    elif(user_input == 3):
        print("search student")
        name = input("Enter name of student: ")
        if search_record(name):
            print("Record not found")

        else:
            for i in stds:
                if i.name == name:
                    print(f"Record of student {name} found.")
                    print(i)
        
    
    elif(user_input == 4):

        print("Update student")
        name = input("Enter name of student: ")
        if search_record(name):
            print("Record not found")
        else:
            for i in stds:
                if i.name == name:
                    print("""
                    Enter 1: To update age
                    Enter 2: To update roll no 
                    Enter 3: To update grade
                    Enter 4: To update address""")
                    option = int(input("please enter number: "))
                    if(option ==1):
                        age = int(input("Enter age: "))
                        i.age = age
                        print("After updated: ")
                        print(i)
                    elif(option == 2):
                        roll_no = int(input("Enter the roll no: "))
                        i.roll_no = roll_no
                        print("After updated: ")
                        print(i)

                    elif(option == 3):
                        grade = int(input("Enter the grade: "))
                        i.grade = grade
                        print("After updated: ")
                        print(i)
                    elif(option == 4):
                        address = input("Enter address of student: ")
                        i.address= address
                        print("After updated: ")
                        print(i)

                    else:
                        quit('Invalid option selected')
    
    elif(user_input == 5):
        print("Delete student")
        name = input("Enter the name: ")
        if search_record(name):
            print("Record not found")
        else:
            j = 0
            for i in stds:
                
                if i.name == name:
                    del stds[j]
                j +=1
        
            

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
   








      

        


