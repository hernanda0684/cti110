# Counting Feet to Inches
# 06/27/2017
# CTI-110 M5T2_FeetToInches 
# Andrae Hernandez-Diaz
#

inches_per_foot = 12

def main():
    feet = int(input('Enter a number of feet: '))

    print(feet, 'equals', feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet * inches_per_foot

main()
