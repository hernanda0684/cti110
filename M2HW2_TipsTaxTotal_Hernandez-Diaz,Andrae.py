# Calculating Tips, Tax, and Total
# Date: 06/06/2017
# CTI-110 M2HW2 - Tips, Tax, Total
# Hernandez-Diaz, Andrae
#
total_charge = float(input('Enter total meal charge: '))
tip = 0.18 * total_charge
tax = 0.07 * total_charge
total = tip + tax + total_charge
print('After Tip_Tax is $', total)
