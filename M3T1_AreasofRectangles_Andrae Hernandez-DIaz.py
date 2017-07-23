# Finding the area of a rectangle (width and height)
# 06/16/2017
# CTI-110 M#T1 - Areas of Rectangles
# Andrae Hernandez-Diaz

length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
        
