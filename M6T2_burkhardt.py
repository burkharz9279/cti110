# This program converts feet to inches
# using a value returning function
# 11/1/2017
# CTI-110 M6T2_FeetToInches 
# Zachary Burkhardt

# Constant for the numbers of inches per foot
INCHES_PER_FOOT = 12

def main():
    # Get a number of feet from the user.
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches.
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

#The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
