def hypot(num1 , num2):
    return (num1**2 + num2**2)**0.5


num1 = float(input("Enter the length of the first side: "))
num2 = float(input("Enter the length of the second side: "))
    
hypotenuse = hypot(num1, num2)
    
print(f"The length of the hypotenuse is: {hypotenuse}")