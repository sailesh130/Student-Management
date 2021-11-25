import os
import platform
global stds
stds = []
from teacher import Supervisor
from student import Student
from faculty import Faculty



def assign_supervisior():
    name = input("Enter the name of supervisor: ")
    address = input("Enter the address of supervisior: ")
    teacher_record = Supervisor(name,address)
    return teacher_record


def choose_subject():
    print("""
    Choose one of the option to choose subject
    Enter 1: Science
    Enter 2: Management
    Enter 3: Arts
    Enter 4: Humanities """)
    option = int(input("Enter the option: "))
    if option == 1:
        subject = "Science"
    elif option == 2:
        subject = "Management"
    elif option == 3:
        subject = "Arts"
    elif option == 4:
        subject = "Humanities"
    else:
        print("Invalid option")
        quit()
    return Faculty(subject)

def search_record(name):
    if name not in [record.name for record in stds]:
        return True

def display_record(stds):
    if len(stds)==0:
            
            print("No student in the record\n")
    else:
        for record in stds:
            print("=> ",record)

def add_new_student():
    name = input("Enter name: ")
    age = int(input("Enter age of student: "))
    roll_no = input("Enter roll no of student: ")
    grade = input("Enter grade of student: ")
    address = input("Enter address of student: ")
    subject = choose_subject()
    supervisior = assign_supervisior()
    

    student_record = Student(name,age,roll_no,grade,address,subject,supervisior)
    print("HEllo")
    print("Added information:")
    print(student_record,"\n")
    stds.append(student_record)
    

def search_student():
    name = input("Enter name of student: ")
    if search_record(name):
        print("Record not found")

    else:
        for record in stds:
            if record.name == name:
                print(f"Record of student {name} found.")
                print(record)
        

def update_student():
    name = input("Enter name of student: ")
    if search_record(name):
        print("Record not found")
    else:
        for record in stds:
            if record.name == name:
                print("""
                    Enter 1: To update age
                    Enter 2: To update roll no 
                    Enter 3: To update grade
                    Enter 4: To update address""")
                option = int(input("please enter number: "))
                if(option ==1):
                    age = int(input("Enter age: "))
                    record.age = age
                    print("After updated: ")
                    print(record)
                elif(option == 2):
                    roll_no = int(input("Enter the roll no: "))
                    record.roll_no = roll_no
                    print("After updated: ")
                    print(record)

                elif(option == 3):
                    grade = int(input("Enter the grade: "))
                    record.grade = grade
                    print("After updated: ")
                    print(record)

                elif(option == 4):
                    address = input("Enter address of student: ")
                    record.address= address
                    print("After updated: ")
                    print(record)

                else:
                    print("'Invalid option selected'")
                    quit()


def delete_student():
    name = input("Enter the name: ")
    if search_record(name):
        print("Record not found")
    else:
        j = 0
        for record in stds:
                
            if record.name == name:
                del stds[j]
            j +=1
    












      

        


