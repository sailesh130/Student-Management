import psycopg2
from main import main,runagain
host = 'localhost'
password = "9843"
port = 5432
database = 'student'
user = "postgres"

try:
    conn = psycopg2.connect(
        host=host,
        database=database, 
        user=user,
        password=password,
        port=port)
    cur = conn.cursor()
    
    script1 = '''CREATE TABLE IF NOT EXISTS student (
                id SERIAL PRIMARY KEY,
                supervisior_id int NOT NULL,
                faculty_id int NOT NULL,
                name varchar(40) NOT NULL,
                age int NOT NULL,
                rollno int NOT NULL,
                grade int,
                address varchar(50),
                CONSTRAINT fk_supervisior FOREIGN KEY (supervisior_id) REFERENCES supervisior(id) ON DELETE CASCADE,
                CONSTRAINT fk_faculty FOREIGN KEY (faculty_id) REFERENCES faculty(id) ON DELETE CASCADE);'''
           
    script2 = '''CREATE TABLE IF NOT EXISTS supervisior (
        id SERIAL PRIMARY KEY,
        name varchar(40) NOT NULL,
        address varchar(40) NOT NULL
    );'''
    
    script3 =  '''CREATE TABLE IF NOT EXISTS subject (
        id  SERIAL PRIMARY KEY,
        faculty_id int NOT NULL,
        name varchar(40) NOT NULL,
        CONSTRAINT fk_faculty FOREIGN KEY (faculty_id) REFERENCES faculty(id) ON DELETE CASCADE
    );'''
    script4 = '''CREATE TABLE IF NOT EXISTS faculty (
        id SERIAL PRIMARY KEY,
        name varchar(50));
        '''
    script5 = '''CREATE TABLE IF NOT EXISTS student_subject (
        student_id int,
        subject_id int,
        PRIMARY KEY (student_id, subject_id),
        CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES student(id) ON DELETE CASCADE ,
        CONSTRAINT fk_subject FOREIGN KEY (subject_id) REFERENCES subject(id) ON DELETE CASCADE
        );'''
    
    cur.execute(script2)
    
    cur.execute(script4)
    
    cur.execute(script1)

    cur.execute(script3)
    cur.execute(script5)
    conn.commit()
    
    print("Table sucessfully created")

    main(cur,conn)
    runagain(cur,conn)
except Exception as error:
    print(error)

finally:
    if conn:
        cur.close()

        conn.close()
        print("Database closed")
