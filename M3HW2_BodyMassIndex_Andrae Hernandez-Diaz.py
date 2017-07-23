# I Need to Know how fat i am through the BMI index
# 06/15/2017
# CTI-110 M3HW2 - Body Mass Index
# Andrae Hernandez-Diaz
#

weight = float(input("Enter your weight(lb): "))
height = float(input("Enter your height(in): "))

# print(height,weight)
bmi = weight * 703/(height**2)
print("BMI: ",bmi)

# else: < 18.5 too skinny
# else: <= 25 optimal
# else: too heavy

if bmi < 18.5:
    print ("Too skinny")
elif bmi <=25:
    print ("Optimal")
else:
    print ("Too heavy")
