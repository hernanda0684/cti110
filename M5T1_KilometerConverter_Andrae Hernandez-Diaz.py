# Counting Numbers
# 06/20/2017
# CTI-110 M5T1_KilometerConverter 
# Andrae Hernandez-Diaz
#

def main():
    kilometers = int(input('Enter a distance in kilometers: '))
    show_miles(kilometers)
    
def show_miles(km):
    miles = km* 0.6214

    print(km, 'kilometers equals', miles, 'miles.')

main()
          
