# CTI 110
# M3 T1
# Zachary Burkhardt
# Late

#Get dimensions of Rectangle 1
length1 = int(input('Enter length of rectangle 1: '))
width1 = int(input('Enter wight of rectangle 1: '))

#Get dimensions of Rectangle 2
length2 = int(input('Enter length of rectangle 2: '))
width2 = int(input('Enter wight of rectangle 2: '))

#Calculate the areas of the rectangles
area1 = length1 * width1
area2 = length2 * width2

#Determine which has greater area
if area1 > area2:
    print('Rectangle 1 has greater area.')
else:
    if area2 > area1:
        print('Rectangle 2 has greater area.')
    else:
        print('Both have the same area.')
    
