# My Bug Collection
# 06/16/2017
# CTI-110 M4T1 - Bug Collector
# Andrae Hernandez-Diaz
#

# Begin the Accumulator
total = 0

# Bugs collected each day.
for day in range(0, 7):
    Collected = input("Enter the bugs collected on day: ")
    bugs = int(input())
    total = total + bugs
    
# Display total bugs.
print('Total bugs collected', total, 'bugs.')
