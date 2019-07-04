class Circle:
    
    def __init__(self,r):
        self.radius = r
    
    def calculation_area(self):
        area = 3.14 * self.radius * self.radius
        print('Area is: ' + str(area))

    def calculation_perimeter(self):
        perimeter =2 * 3.14 * self.radius
        print('Perimeter is: ' + str(perimeter))

    #def diffrence(self):
     #   diff = int(area) - int(perimeter)

c = Circle(5)
c.calculation_area()
c.calculation_perimeter()
