1)
gender=input("enter gender male or female")
if gender=="male":
    print("u entered correct input")
elif gender=="female":
    print("u enter correct input")
else:
    print("plz enter correct gender male or female")


2)
gender=input("enter gender male or female ")
name=input("enter name")
if gender=="male":
    print("Hello %s ,sir"%name)
elif gender=="female":
    print("Hello %s ,mam"%name)
else:
    print("plz enter correct gender male or female")


3)
try:
    age=int(input("enter age of female "))
except ValueError:
    print("i donot understand")
else:
    if age>20 :
            print("you are able to enroll for python fundamental")
    else:
            print("you are below the age criteria nd not able to enroll the course")


4)
try:
    age=int(input("enter age of female "))
except ValueError:
    print("i donot understand")
else:
    if age>19 :
        print("you are able to enroll for java course")
    else:
        print("you are below the age criteria nd not able to enroll the course")


5)
name=input("enter the name")
if name.isdigit():
    print("plz enter alphabet value")
elif name.isalpha():
    print(name)
else:
    print("enter something")
