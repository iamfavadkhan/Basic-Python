class Employee:
    name = " "
    age = 0
    salary = 0.0
    def __init__(self , name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
        
employee1 = Employee("Fawad" , 20 , 500.0)
employee2 = Employee("Hamza" , 22 , 5000.0)
employee1.display()
employee2.display()