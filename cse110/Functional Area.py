import math
pi = math.pi

repeater = True

def rect_area(side_len1, side_len2):
    area = side_len1 * side_len2
    return area

def square_area(side_len1):
    area = rect_area(side_len1, side_len1)
    return area

def circle_area(side_len1):
    area = (pi * (side_len1 ** 2))
    return area

def area_finder(shape):
    if shape.find('square') != -1:
        side_len1 = int(input('What is the side length?  '))
        area = square_area(side_len1)
        return area
    elif shape.find('circle') != -1:
        side_len1 = int(input('What is the length of the radius?  '))
        area = circle_area(side_len1)
        return area
    elif shape.find('rectangle') != -1:
        side_len1 = int(input('What is the first side length?  '))
        side_len2 = int(input('What is the second side length?  '))
        area = rect_area(side_len1, side_len2)
        return area
    else:
        print('I\'m sorry that doesn\'t seem right...')

while (repeater):
    shape = input('What is the shape in question? (square, circle, rectangle)(type \'quit\' when done)  ').lower()
    if shape.find('quit') != -1:
        repeater = False
    else:
        area = area_finder(shape)
        print(area)
    
    
