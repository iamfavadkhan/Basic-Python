# 1. Constructor Basics with Validation
# Create a BankAccount class with:
# __init__ to set account_number and balance.
# If balance is less than 0, raise a ValueError.
# A method deposit(amount) to add money.
# A method withdraw(amount) to deduct money only if sufficient balance exists.

class BankAccount:
    def __init__(self , account_number , balance):
        self.account_number = BankAccount
        self.balance = balance
        if balance < 0.0:
            raise ValueError("Balance cannot be negative")

    def deposit_amount(self, amount):
        self.amount = amount
        self.balance += amount

    def with_draw_amount(self , with_draw):
        self.with_draw = with_draw
        self.balance = self.balance - self.with_draw
        
        
bankAccount = BankAccount(12345, 5000.0)
bankAccount.with_draw_amount(200.0)
bankAccount.deposit_amount(500.0)
bankAccount.with_draw_amount(300.0)
bankAccount.with_draw_amount(3000.0)


print(f"Final Balance in your account is :${bankAccount.balance}")
      