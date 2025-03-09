from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self, id, name, age, balance):
        self.id = id
        self.name = name
        self.age = age
        self.balance = balance

    def info(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "balance": self.balance
        }

    @abstractmethod
    def withdraw(self, amt):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def deposit(self, amt):
        pass

class User(Bank):
    def __init__(self, id, name, age, balance):
        super().__init__(id, name, age, balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print(f"Limit exceeded! You only have {self.balance}.")
            return
        self.balance -= amt
        print(f"Withdrawal successful! You withdrew {amt}.")
        self.check_balance()

    def check_balance(self):
        print(f"Your bank balance: {self.balance}")

    def deposit(self, amt):
        self.balance += amt
        print(f"Deposit successful! You deposited {amt}.")
        self.check_balance()

# Creating a User instance
sarvesh = User(1, "Sarvesh", 22, 4000)

# Testing the functionalities
print("User Information:", sarvesh.info())

sarvesh.deposit(1000)   # Should increase balance
sarvesh.withdraw(3000)  # Should decrease balance
sarvesh.withdraw(4000)  # Should give an error (exceeds balance)
