#  Question 1
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return (self.x, self.y, self.z)

# Now we can create an instance of Point3D and print its coordinates:
my_point = Point3D(1, 2, 3)
print(my_point.get_coordinates())
 # The output will be:
(1, 2, 3)



#  Question 2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


my_rectangle = Rectangle(length=4, width=3)
print("Area:", my_rectangle.area())  # prints 12
print("Perimeter:", my_rectangle.perimeter())  # prints 14




#  Question 3




import math


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_inside(self, point):
        return math.dist(self.center, point) <= self.radius
center = (0, 0)
radius = 5
my_circle = Circle(center, radius)

# compute area and perimeter
print("Area:", my_circle.area())         # prints 78.53981633974483
print("Perimeter:", my_circle.perimeter())   # prints 31.41592653589793

# check if point is inside the circle
point1 = (3, 4)
point2 = (6, 8)
print("Is point1 inside the circle?", my_circle.is_inside(point1))  # prints True
print("Is point2 inside the circle?", my_circle.is_inside(point2))  # prints False




#  Question 4


class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance
my_account = Bank(100)
print("Initial balance:", my_account.get_balance())    # prints 100

my_account.deposit(50)
print("Balance after deposit:", my_account.get_balance())   # prints 150

my_account.withdraw(75)
print("Balance after withdrawal:", my_account.get_balance())  # prints 75

my_account.withdraw(100)
print("Balance after withdrawal:", my_account.get_balance())  # prints "Insufficient balance"







