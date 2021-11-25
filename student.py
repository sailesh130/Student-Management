from person import Person
class Student(Person):
    def __init__(self,name,age,roll_no,grade,address,subject,supervisior):
        super().__init__(name,address)
        self.age = age
        self.roll_no = roll_no
        self.grade = grade
        self.subject = subject
        self.supervisior = supervisior
        
    def __str__(self):
        return f"""
        Name:{self.name.capitalize()}
        Age:{self.age} 
        Roll no:{self.roll_no}
        Grade: {self.grade}
        Address: {self.address}
        Faculty: {self.subject.name}
        Supervisior: {self.supervisior.name}"""

    def __del__(self):
        print (f"deleted {self.name} record.")
    