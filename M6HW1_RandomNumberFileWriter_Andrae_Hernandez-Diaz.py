# Random number stuff 
# Date
# CTI-110 M6HW1 - Random Number File Writer
# Your Name
#

import random

myfile = open('numbers.txt', 'w')

for count in range(500):
    number = random.randint(1, 500)
    myfile.write(str(number) + '\n')

myfile.close()
print('Done')
