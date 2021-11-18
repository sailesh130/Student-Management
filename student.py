class Student():
    def __init__(self,name,age,roll_no,grade,address,subject,supervisior):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.grade = grade
        self.address = address
        self.subject = subject
        self.supervisior = supervisior
        
    def __str__(self):
        return f"""
        Name:{self.name.capitalize()}
        Age:{self.age} 
        Roll no:{self.roll_no}
        Grade: {self.grade}
        Address: {self.address}
        Subject: {self.subject}
        Supervisior: {self.supervisior.name}"""

    