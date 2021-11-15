class Supervisor:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def __del__(self):
        print("Supervisior information deleted")