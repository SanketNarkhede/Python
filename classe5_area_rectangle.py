class Rectangle:
    def __init__(self,l,b):
        self.length = l
        self.breadth =b

    def area(self):
        area = self.length * self.breadth

        print("Area is: " + str(area))

r = Rectangle(5,6)
r.area()