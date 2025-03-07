class ComplexNumber:
  def __init__(self,x,y):
      self.x = x
      self.y = y

  def __add__(self, other):
      return ComplexNumber(self.x +other.x,self.y+other.y)
  def __str__(self):
      return f"{self.x},{self.y}"

s = ComplexNumber(2,4)
a = ComplexNumber(4,5)
print(s+a)