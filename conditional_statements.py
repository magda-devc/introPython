x = 10
y = 20
if x < y and y > 30:
    print("TRUE")
else:
    print("FALSE")

if x<y or y>30:
    print("TRUE")
else:
    print("FALSE")

marks = 90
if marks< 40:
    print("E")
elif marks<50:
    print("D")
elif marks<60:
    print("C")
elif marks<70:
    print("B")
else:
    print("A")

bettingnumber = 0
if bettingnumber == 1:
    print("You won a goat!!")
elif bettingnumber == 2:
    print("You won a cow!!")
elif bettingnumber == 3:
    print("You wo 3 cows!!")
elif bettingnumber == 4:
    print("You won 5 cows!!")
else:
    print("Please enter a number from 1 - 4 to bet!!")

p = 100000
r = 8
t = 2
interest = (p*r*t)/100
if interest < 8000:
    print("Good loan")
elif interest <12000:
    print("Bad loan")
else:
    print("Scam")


weight = 50
height = 1.65
BMI = weight/ (height*height)
print("BMI =",BMI)
if BMI <=18:
    print("Underweight")
elif BMI <=29:
    print("Normal weight")
elif BMI <=34:
    print("Over weight")
else:
    print("Obese")