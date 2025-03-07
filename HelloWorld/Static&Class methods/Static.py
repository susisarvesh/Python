class MathUtils:
    def __init__(self):
        print("Static method does not belongs to class not objects so it does not use this:")
    @staticmethod
    def addition(n1,n2):
        return n1 + n2

    @staticmethod
    def multiplication(n1,n2):
        return n1 * n2

    @staticmethod
    def Logger():
        print("Logged")

math =  MathUtils()
print(MathUtils.addition(2,3))
math.Logger()


