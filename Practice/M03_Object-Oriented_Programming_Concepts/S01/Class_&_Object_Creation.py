class Example:
    x = 100
    def display(self):
        print("This is Example class display method")
obj = Example()
obj.display()
print(obj.x)


#class cirlce with two methods - area , perimeter
from math import pi
class Circle:
    r = 7
    def area(self):
        return pi *self.r *self.r
    def perimeter(self):
        return 2 * pi * self.r
c = Circle()
print(c.area())
print(c.perimeter())    
print(dir(c))