##Define an abstract class Animal with an abstract method make_sound(). Implement it in Dog and Cat classes.
from  abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Bow Bow")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")
browny  = Dog()
browny.make_sound()


##Implement an abstract class Appliance with abstract methods turn_on() and turn_off(). Create TV and Fan classes
class Appliances(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class Tv(Appliances):
    def turn_on(self):
        print("tv turn on")
    def turn_off(self):
        print("tv turn off")
class Fan(Appliances):
    def turn_on(self):
        print("Fan turn on")
    def turn_off(self):
        print("Fan turn off")
samsung = Tv()
samsung.turn_off()