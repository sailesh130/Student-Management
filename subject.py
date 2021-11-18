class Subject:
    def __init__(self,name,teacher_id,student_id):
        self.name = name
        self.teacher_id = teacher_id
        self.student_id = student_id
    def __str__(self) -> str:
        return f'''
                Subject name: {self.name}'''