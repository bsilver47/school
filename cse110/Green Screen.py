#255
from PIL import Image
print('Success is assured')

pick_picture = pp = int(input('What is your object image? (1-8)  '))
back_picture = bp = int(input('What is your background image (1-7)  '))
effect = int(input('What effect would you like to employ?  '))


if pick_picture == 1:
    pick_picture = Image.open('spaceshuttle.jpg')
elif pick_picture == 2:
    pick_picture = Image.open('penguin.jpg')
elif pick_picture == 3:
    pick_picture = Image.open('hiker.jpg')
elif pick_picture == 4:
    pick_picture = Image.open('harvester.jpg')
elif pick_picture == 5:
    pick_picture = Image.open('cat.jpg')
elif pick_picture == 6:
    pick_picture = Image.open('cat_small.jpg')
elif pick_picture == 7:
    pick_picture = Image.open('cactus.jpg')
else:
    pick_picture = Image.open('boat.jpg')

if back_picture == 1:
    back_picture = Image.open('sunset.jpg')
elif back_picture == 2:
    back_picture = Image.open('snowscape.jpg')
elif back_picture == 3:
    back_picture = Image.open('forest.jpg')
elif back_picture == 4:
    back_picture = Image.open('field.jpg')
elif back_picture == 5:
    back_picture = Image.open('earth.jpg')
elif back_picture == 6:
    back_picture = Image.open('desert.jpg')
else:
    back_picture = Image.open('beach.jpg')

width, height = back_picture.size

pixels_primary = pick_picture.load()
pixels_secondary = back_picture.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels_primary[i, j]
        if ((i == 5) and (j == 10)) or ((i == 15) and (j == 20)) or ((i == 25) and (j == 30)) or ((i == 35) and (j == 40)) or ((i == 45) and (j == 50)):
            print(f'{r}, {g}, {b}')
        if (g >= 200) and (r < 100) and (b < 100):
            r, g, b = pixels_secondary[i, j]
            pixels_primary[i,j] = pixels_secondary[i,j]
        
        #nofilter
        if effect == 0:
            r, g, b = r, g, b
        #greyscale
        elif effect == 1:
            r = g = b = round((r + g + b) / 3)
        #sepia (looked up conversion)
        elif effect == 2:
            tempr = round(0.393 * r + 0.769 * g + 0.189 * b)
            tempg = round(0.349 * r + 0.686 * g + 0.168 * b)
            tempb = round(0.272 * r + 0.534 * g + 0.131 * b)
            r = tempr
            g = tempg
            b = tempb
        #inverted picture 1 (experimenting)
        elif effect == 3:
            tempr = round((g + b) / 2)
            tempg = round((r + b) / 2)
            tempb = round((r + g) / 2)
            r = tempr
            g = tempg
            b = tempb
        #inverted picture 2 (experimenting)
        else:
            r = 255 - r
            g = 255 - g
            b = 255 - b

        pixels_primary[i, j] = (r, g, b)
        if ((i == 5) and (j == 10)) or ((i == 15) and (j == 20)) or ((i == 25) and (j == 30)) or ((i == 35) and (j == 40)) or ((i == 45) and (j == 50)):
            print(f'{r}, {g}, {b}')

pick_picture.save(f'new_picture_{pp}+{bp}.jpg')

#image_main.show()
#image_main.save('the_file_goes_here.jpg')