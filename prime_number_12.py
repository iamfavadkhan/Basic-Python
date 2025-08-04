# ask the user for a number
# and determine whether the 
# number is prime or not. 
#(For those who have forgotten,
# prime number is a number that has no divisors.). 

number = int(input("Enter a number "))
counter = 0

for i in range(1,number+1):
    if number%i==0:
        counter+=1
if counter == 2:
    print(f"Prime number :{number}")
else:
    print(f"composite number :{number}")