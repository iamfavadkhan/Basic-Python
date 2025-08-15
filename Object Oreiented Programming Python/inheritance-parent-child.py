class Parent:
    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname
    def show(self):
        print(f"First Name: {self.fname}, Last Name: {self.lname}")
        
class Child(Parent):
    def __init__(self , fname , lname , age):
        super().__init__(fname , lname)
        self.age = age
    def show(self):
        super().show()
        print(f"Age: {self.age}")


child1 = Child("Fawad" , "Khan", 20)
child1.show()
    