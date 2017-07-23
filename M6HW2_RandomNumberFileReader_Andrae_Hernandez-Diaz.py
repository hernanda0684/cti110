# Reading Random Numbers
# Date
# CTI-110 M6HW2 - Random Number File Reader
# Your Name
#

myfile = open('numbers.txt', 'r')

line = myfile.readline()

while line != '':
    print(line, end='')
    line = myfile.readline()

myfile.close()
