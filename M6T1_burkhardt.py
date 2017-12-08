#CTI 110
#M6 T1: Kilometer Converter
#Zachary Burkhardt
#10/30/2017

CONVERSION_FACTOR = 0.6214

def main():
    #Get distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance in kilometers
    show_miles(kilometers)
    
def show_miles (km):
    #Calculate miles
    miles = km * CONVERSION_FACTOR

    #Display the miles
    print(km, 'kilometers equals', miles, 'miles.')

#Call the main function
main()
