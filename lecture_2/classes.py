class Point():
    def __init__(self, input1, input2):
        #properties of the class
        # property x
        self.x = input1
        # property y
        self.y = input2

# instantiate the class
# create an object of the class, point p, which calls the init function implicitly
p = Point(2, 8)
# after creating the object, we can access the properties of the object
print(p.x)
print(p.y)