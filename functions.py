import math


def motto():
    print("Hello there is our motto")

motto()
def vision():
    print("This is our vision")

vision()

def add():
    x = 10
    y = 20
    z = x+y
    print(z)

add()

def avg(x, y, z):
    average = (x +y +z)/ 3
    print("Your average is " +str(average))

avg(12, 34, 56)
avg(40, 78, 40)

def bmicalc(weight, height):
    bmi = weight / pow(height, 2)
    if bmi <=18:
        print("Underweight")
    elif bmi <= 29:
        print("Normal weight")
    elif bmi <=34:
        print("Over weight")
    else:
        print("Obese")

bmicalc(50, 1.65)

def marks(marks):
    if marks <= 40:
        print("E")
    elif marks <= 50:
        print("D")
    elif marks <= 60:
        print("C")
    elif marks <= 70:
        print("B")
    else:
        print("A")
marks(64)

def login(email, password):
    if email == "user@example.com" and password == "user123":
        marks(71)
    else:
        print("Login failed")

login("user@example.com", "user123")

def areaofacircle(radius):
    area = math.pi * pow(radius, 2)
    return area

print(areaofacircle(10))