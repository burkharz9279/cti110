#CTI 110
#M3 HW2
#Zachary Burkhardt
#9/20/2017

def main():
    quantity = float(input('Enter amount of packages purchased: '))
    totalCost = quantity * 99
    discount = 0
    if quantity <= 9:
        print ('Your total is: ', totalCost)
    elif quantity >= 10 and quantity < 20:
        discount = 0.9
        print('You qualify for a 10% discount!\nYour total is: ', round(totalCost * discount, 2))
    elif quantity >= 20 and quantity < 50:
        discount = 0.8
        print ('You qualify for a 20% discount!\nYour total is: ', round(totalCost * discount, 2))
    elif quantity >= 50 and quantity < 100:
        discount = 0.7
        print ('You qualify for a 30% discount!\nYour total is: ', round(totalCost * discount, 2))
    else:
        discount = 0.6
        print ('You qualify for a 40% discount!\nYour total is: ', round(totalCost * discount, 2))
main()
