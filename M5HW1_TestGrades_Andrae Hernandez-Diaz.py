# Average Test Scores
# 06/27/2017
# CTI-110 M5HW1 - Test Average and Grade
# Andrae Hernandez-Diaz
#

def calc_Average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    print ("Your average score is:", average)
    
    
def determine_grade(score):
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    elif  score <= 100:
        return "A"

def get_score():
    score1 = int(input("Enter 1st score: "))
    score2 = int(input("Enter 2nd score: "))
    score3 = int(input("Enter 3rd score: "))
    score4 = int(input("Enter 4th score: "))
    score5 = int(input("Enter 5th score: "))
    
    return score1, score2, score3, score4, score5

def printTableOfResults ( score1, score2, score3, score4, score5 ):
    print("Score\t Letter Grade")
    print()
    print(  str (score1) + "\t\t" + determine_grade(score1), \
            str (score2) + "\t\t" + determine_grade(score2), \
            str (score3) + "\t\t" + determine_grade(score3), \
            str (score4) + "\t\t" + determine_grade(score4), \
            str (score5) + "\t\t" + determine_grade(score5), sep = "\n")

    return score1, score2, score3, score4, score5

def main():
    score1, score2, score3, score4, score5 = get_score()
    print()
    printTableOfResults (score1, score2, score3, score4, score5)
    calc_Average(score1, score2, score3, score4, score5)
    
    
main()
