#CTI 110
#M3HW1 - Age Classifier
#Zachary Burkhardt
#9/18/17

def main():
    age = int(input('What is your age? '))
    if age <= 1:
        print('You are an infant.')
    elif age > 1 and age < 13:
        print('You are a child.')
    elif age > 13 and age < 20:
        print('You are a teen.')
    else:
        print('You are an adult.')
main()
