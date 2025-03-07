##Implement method overriding in a Vehicle class with Car and Bike subclasses.

class Vehicle:
    def Smoke(self):
        print("This is vehicle Produces Smoke")
class Car(Vehicle):
    def Smoke(self):
        print("This is Car Produces Smoke")
class Bike(Vehicle):
    def Smoke(self):
        print("This is Bike Produces less Smoke")
honda = Car()
honda.Smoke()