import os
import platform
global stds
stds = []
from teacher import Supervisor
from student import Student

def assign_faculty(cur,conn):
    name1 = input("Enter the faculty name: ")
    cur.execute("SELECT id from faculty where name=%s ",(name1,))
    id = cur.fetchone()
    if id:
        return id[0]
    else:
        cur.execute("INSERT INTO faculty(name) VALUES(%s)",(name1,))
        conn.commit()
        print("Faculty added.")
        cur.execute("SELECT id from faculty WHERE name = %s",(name1,))
        return cur.fetchone()[0]


def assign_supervisior(cur,conn):
    name = input("Enter the name of supervisor: ")
    address = input("Enter the address of supervisior: ")
    cur.execute("SELECT id FROM supervisior WHERE name=%s AND address=%s ",(name,address))
    id = cur.fetchone()
    if (id):

        return id[0]
        
        
    else:
        cur.execute("INSERT INTO supervisior (name,address) VALUES(%s, %s)",(name,address))
        conn.commit()
        print("Supervisior information added")
        cur.execute("SELECT id from supervisior WHERE name = %s",(name,))
        record = cur.fetchone()[0]
        return record
    


def choose_subject(std_id,fac_id,cur,conn):
    while(True):
        subject_name = input("Enter the name of subject: ")
        cur.execute("SELECT id from subject WHERE name=%s AND faculty_id=%s ",(subject_name,fac_id))
        id = cur.fetchone()
        if id:
            sub_id = id[0]
        else:

            cur.execute("INSERT INTO subject (faculty_id,name) VALUES(%s,%s)",(fac_id,subject_name))
            conn.commit()
            cur.execute("SELECT id from subject WHERE name = %s",(subject_name,))
            sub_id = cur.fetchone()[0]
        cur.execute("INSERT INTO student_subject(student_id,subject_id) VALUES(%s,%s)",(std_id,sub_id))
        conn.commit()
        print("Subject saved in database.\n")
        print("""
                Enter 1: to exit
                Enter 2: To enter next subject""")
        option = int(input("Enter the option: "))
        if option == 1:
            break
        elif option ==2:
            continue
        else:
            print("Invalid opton")
            quit()
        
    
    

def search_record(name,cur):
    cur.execute("SELECT * from student WHERE name=%s",(name,))
    record = cur.fetchone()
    if not record:
        return True

def display_record(records):
    if not records:
            
            print("No student in the record\n")
    else:
        for record in records:
            print(f"""=>
             ID :{record[0]}
             Name: {record[3]}
             Age: {record[4]}
             Roll no: {record[5]}
             Grade: {record[6]}
             Address: {record[7]} """)

def add_new_student(cur,conn):
    name = input("Enter name: ")
    age = int(input("Enter age of student: "))
    roll_no = input("Enter roll no of student: ")
    grade = input("Enter grade of student: ")
    address = input("Enter address of student: ")
    
    sup_id = assign_supervisior(cur,conn)
    fac_id = assign_faculty(cur,conn)

    
    
    cur.execute("INSERT INTO student(supervisior_id,faculty_id,name,age,rollno,grade,address) \
        VALUES (%s,%s,%s,%s,%s,%s,%s)",(sup_id,fac_id,name,age,roll_no,grade,address));
    conn.commit()
    print("Student information added")
    cur.execute("SELECT id FROM student WHERE name=%s",(name,))
    std_id = cur.fetchone()[0]
    choose_subject(std_id,fac_id,cur,conn)
    

def search_student(cur):
    name = input("Enter name of student: ")
    if search_record(name,cur):
        print("Record not found")

    else:
        cur.execute("SELECT * from student WHERE name=%s",(name,))
        record = cur.fetchone()
        print(f"""
                Name: {record[3]}
                Age:    {record[4]}
                Roll n0: {record[5]}
                Grade:  {record[6]}
                Address: {record[7]}""")
        

def update_student(cur,conn):
    name = input("Enter name of student: ")
    if search_record(name,cur):
        print("Record not found")
    else:
        
    
        print("""
                    Enter 1: To update age
                    Enter 2: To update roll no 
                    Enter 3: To update grade
                    Enter 4: To update address""")
        option = int(input("please enter number: "))
        if(option ==1):
                    age = int(input("Enter age: "))
                    cur.execute("UPDATE student SET age=%s WHERE name=%s",(age,name))
                    conn.commit()
                    print("Age updated ")
                    
        elif(option == 2):
                    roll_no = int(input("Enter the roll no: "))
                    cur.execute("UPDATE student SET rollno=%s WHERE name=%s",(roll_no,name))
                    conn.commit()
                    print("Roll no updated ")

        elif(option == 3):
                    grade = int(input("Enter the grade: "))
                    cur.execute("UPDATE student SET grade=%s WHERE name=%s",(grade,name))
                    conn.commit()
                    print("Grade updated ")

        elif(option == 4):
                    address = input("Enter address of student: ")
                    cur.execute("UPDATE student SET address=%s WHERE name=%s",(address,name))
                    conn.commit()
                    print("Address updated ")

        else:
                    print("'Invalid option selected'")
                    quit()


def delete_student(cur,conn):
    name = input("Enter the name: ")
    if search_record(name,cur):
        print("Record not found")
    else:
        cur.execute("DELETE from student WHERE name = %s",(name,))
        conn.commit()
        print("Student record deleted")