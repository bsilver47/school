def realfeel(temp, wind_speed):
    feel = 35.74 + (0.6215 * temp) - (35.75 * wind_speed) + (0.4275 * temp * wind_speed)
    return feel

pointer = []
def counter():
    x = 5
    while x < 65:
        pointer.append(x)
        x += 5

def caution(feel):
    if feel < -50:
        warning = 'Danger! At this temperature, if more than 5 minutes is spent outside at a time, frostbite is likely!'
    elif feel < -30:
        warning = 'Warning! At this temperature, if more than 10 minutes is spent outside at a time, frostbite is likely!'
    elif feel < -5:
        warning = 'Caution! At this temperature, if more than 30 minutes is spent outside at a time, frostbite is likely!'
    else:
        warning = 'Enjoy the weather!'
    return warning

temp = float(input('What is the temperature? '))
unit = input('Is that in Celsius or Fahrenheit? ').lower()
if unit.find('c') != -1:
    ftemp = ((temp * 9 /5) + 32)
else:
    ftemp = temp
counter()
for x in pointer:
    wind_speed = x ** 0.16
    feel = realfeel(ftemp, wind_speed)
    warning = caution(feel)
    print(f'At {ftemp} degrees Fahrenheit, and windspeed of {x} miles per hour, the RealFeel temperature would be {feel:.02f}.')
    print(warning)
