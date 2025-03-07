class Shape:
    def area(self,a=None,b =None ,c =None):
        if a !=None and b!=None and c !=None:
            return a+b+c
        if a != None and b != None and c == None:
            return a + b
        if a != None and b == None and c == None:
            return a
Rec  = Shape()
Circ = Shape()
print(Rec.area(1,2,3))
print(Circ.area(100,200))
