#CTI 110
#M5 T2
#Zachary Burkhardt
#10/9/17

def main():

    #Initialize the accumulator.
    totalBugs = 0

    #Get the bugs collected for each day.
    for day in range (1, 8):
        print ('Enter the bugs collected on day', day)
        bugs = int(input())
        totalBugs += bugs

    #Display the total bugs.
    print ('You collected a total of', totalBugs, 'bugs')

main()
