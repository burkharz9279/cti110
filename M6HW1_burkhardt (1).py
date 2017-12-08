# This program asks the user to enter 5 test grades, calcuates the average,
# displays a letter for each grade and displays the average.
# 11/6/2017
# CTI-110 M6HW1 - Test Average and Grade
# Zachary Burkhardt

def main():

    total = 0
    a = 0

    while a < 5:
        grade = int(input("Enter test score: "))
        print(determine_grade(grade))
        total += grade
        a += 1

    average = calc_average(total)
    grade = determine_grade(average)
    print(average)
    print(grade)

def calc_average (score):
    average = score/5
    return average

    '''grade = determine_grade(average)
    print(grade)'''

def determine_grade (score):
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"
        
main()
