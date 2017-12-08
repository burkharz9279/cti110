#CTI 110
#M3 Lab
#Zachary Burkhardt
#9/18/17

def main():
    score = int(input('Enter grade: '))
    if score >= 90:
        print('Your grade is: A')
    elif score < 90 and score >= 80:
        print('Your grade is: B')
    elif score < 80 and score >= 70:
        print('Your grade is: C')
    elif score < 70 and score >= 60:
        print('Your grade is: D')
    else:
        print('Your grade is: F')
main()
