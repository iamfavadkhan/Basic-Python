import random

def check(user , comp):
    if (comp == user):
        return 0
    elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
        return 1
    else:
        return -1


user = int(input("0 for snake , 1 for gun and 2 for water :"))
comp = random.randint(0,2)

score = check(user , comp)
if score == 0:
    print("Its draw")
elif score == 1:
    print("You Win")
else:
    print("You Lose")
    
print("You chose :",user)
print("Computer chose :",comp)
    