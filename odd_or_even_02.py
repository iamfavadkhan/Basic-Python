# The exercise comes first (with a few extras if you want the extra
# challenge or want to spend more time), followed by a discussion.
# Enjoy! Ask the user for a number. Depending on whether the number
# is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

while True:
    number = input("Enter a number OR Enter done to break the loop :")
    if number.lower() == "done":
        break
    try:
        if int(number) % 2 == 0:
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")
    except ValueError:
        print("You entered Invalid input")