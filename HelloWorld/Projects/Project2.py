import random
import string

class PasswordGenerator:
    def __init__(self):
        self.Question()

    def Question(self):
        ask = input(("DO you want to generate a password>>>?"))
        if ask == "y" or ask == "Y":
            self.password()
        else:
            print("Ok Thanks byee..")
            self.Question()
    def password(self):
        nums = random.randint(20000,478722)
        name  = input("Enter your NAME please >>\n")
        length = 8
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        print(name+random_string+str(nums))

passw = PasswordGenerator()