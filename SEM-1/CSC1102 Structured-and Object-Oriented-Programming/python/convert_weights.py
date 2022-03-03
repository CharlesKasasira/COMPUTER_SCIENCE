weight = int(input('Enter weight'))
unit = input('(k) or (l)')

if unit.upper() == 'K':
    converted = weight/0.45
    print('Weight in l: ' + str(converted))
elif unit.upper() == 'L':
    converted = weight*0.45
    print('Weight in k: ' + str(converted))
else:
    print('invald option')