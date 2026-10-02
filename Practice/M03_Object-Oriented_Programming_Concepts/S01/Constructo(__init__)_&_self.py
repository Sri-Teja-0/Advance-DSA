'''from math import pi
class Circle:
    r = 7
    count = 0
    def __init__(self):
        Circle.count += 1
    def area(self):
        return pi *self.r *self.r
    def perimeter(self):
        return 2 * pi * self.r
c1 = Circle()
c2 = Circle()
c3 = Circle()
print(Circle.count)'''


#1603 Design Parking System
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.vehicle  =[big,medium,small]

    def addCar(self, carType: int) -> bool:
        if carType == 1 :
            if self.vehicle[0] > 0: 
                self.vehicle[0]-=1
                return True
        elif carType == 2:
            if self.vehicle[1] > 0:
                self.vehicle[1]-=1
                return True
        elif carType == 3:
            if self.vehicle[2] > 0:
                self.vehicle[2]-=1
                return True
        return False
input = ["ParkingSystem","addCar","addCar","addCar","addCar"]
data = [[1,1,0],[1],[2],[3],[1]]
print(data)             