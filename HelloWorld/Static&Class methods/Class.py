class Student :
    counter =0
    def __init__(self):
        Student.Incremnt()
    @classmethod
    def Incremnt(cls):
        cls.counter+=1
stu = Student()
Student.Incremnt()
print(Student.counter)