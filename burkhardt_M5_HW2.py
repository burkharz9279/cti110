#CTI 110
#M5 HW2
#Zachary Burkhardt
#Late

def main():
    runningTotal = 0

    number = int(input('Enter a number: '))
    runningTotal = runningTotal + number

    while number > -1:
        number = int(input('Enter a number: '))
        if number < 0:
            runningTotal = runningTotal
        else:
            runningTotal = runningTotal + number
    
    print('Total: ', runningTotal)
main()
