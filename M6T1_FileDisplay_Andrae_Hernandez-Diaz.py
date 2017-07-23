# Showing what's in here
# Date
# CTI-110 M5T1 - File Display
# Your Name
#

myfile = open('numbers.txt', 'r')
  
for line in myfile:
    number = int(line)
    print(number)

myfile.close()
