# Finding the area of a rectangle (width and height)
# 06/13/2017
# CTI-110 M3HW1 - Age CLassifier
# Andrae Hernandez-Diaz

userAge = int(input('Please enter your age: '))

if userAge <= 1:
    print("You are an infant")
elif userAge < 13:
    print("You are a child")
elif userAge < 20:
    print("You are a teenager")
elif userAge >= 20:
    print("You are an adult")
    
