# 2. Class Method for Object Creation
# Create a Student class that:
# Accepts name and marks in its constructor.
# Has a class method from_string(cls, data) that takes a string like "Ali-85" and creates a Student object.
class Student:
    def __init__(self , name=None , marks=None):
        self.name = name
        self.marks = marks
    @classmethod
    def from_string(cls, data):
        cls.name, cls.marks = data.split('-')
        print(f"Name : {cls.name}, Marks : {cls.marks}")
 
student1 = Student.from_string("Ali-85")