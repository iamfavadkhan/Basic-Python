a = int(input("Enter num1 :"))
b = int(input("Enter num2 :"))


print("1. Addition")
print("2. Subtraction")
print("3. Mulitiplication")
print("4. Division")

choice = int(input())

if choice == 1:
    print(a ," + " ,b, " = ", a+b)
elif choice == 2:
    print(a , " - ",b ," = ", a-b)
elif choice == 3:
    print(a , " X ",b ," = ", a*b)
elif choice == 4:
    print(a , " / ",b ," = ", a/b)

    
