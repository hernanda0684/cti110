# Counting grades
# 06/15/2017
# CTI-110 M3T2 - Counting Grades
# Andrae Hernandez-Diaz
#

# Grade thresholds
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Test score from user.
score = int(input('Enter the test score: '))

if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score: 
                print('Your grade is D.')
            else:
                print('Your grade is F.')
    
