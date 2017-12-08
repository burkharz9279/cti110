#CTI 110
#M5 HW1: Distance Traveled
#Zachary Bukhardt
#10/23/17

def main():
    
    speed = int(input('Enter the vehicles speed: '))
    time = int(input('Enter the hours traveled: '))
    print('Hour', '    ', 'Distance Traveled')
    print('---------------------------')

    for currentHour in range(1, time+1):
        distance = speed*currentHour
        print (currentHour, '       ', distance)

main()
