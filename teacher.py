class Supervisor:
    def __init__(self,name,address,subject):
        self.name = name
        self.address = address
        self.subject = subject

    def __str__(self) -> str:
        return f'''
                Teacher name: {self.name}
                '''