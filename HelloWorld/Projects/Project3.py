import random


class RPS:
    def __init__(self):
        self.getinputs()
    def getinputs(self):
        print("We are going to Play Rock paper and scissor Lets start!!")
        print("Rock is 0")
        print("Paper is 1")
        print("Scissor is 2")
        user = int(input("Enter your input >> \n"))
        if user not in [0,1,2]:
            print("Please enter nums between 0-2")
            self.getinputs()
        else:
            self.Play(user)

    def Play(self,user):
        choises = [0,1,2]
        ran = random.randint(0,2)
        if choises[ran] == user:
            print("We are same now lets play one more time??\n")
            self.getinputs()
        if (choises[ran] == 0 and user == 2) or (choises[ran] == 1 and user == 0) or (choises[ran] == 2 and user == 1):
            print("You Lost , idiot")
        else:
            print("Congrats ,You win my boss")
sar = RPS()