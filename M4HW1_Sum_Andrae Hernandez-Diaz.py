# Counting Numbers
# 06/20/2017
# CTI-110 M4HW1 - Sum of Numbers
# Andrae Hernandez-Diaz
#

total = 0
userNumber = int(input('Enter the first number or a negative number to quit: '))

while userNumber > -1:
    total = total + userNumber
    userNumber = int(input('Enter the next number or a negative number to quit: '))
    
print('This sum of the numbers is', total)
