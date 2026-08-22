import math

class Circle:
    

    def __init__(self,radius):
        self.radius =radius

    def area(self):
        return (math.pi * pow(self.radius,2))
    
    def perimeter(self):
        return 2*(math.pi)*(self.radius)

radius = float(input("give Radius \n"))

c1 = Circle(radius)



if __name__ == '__main__':
    print(math.floor(c1.area()))
    print(c1.perimeter())

