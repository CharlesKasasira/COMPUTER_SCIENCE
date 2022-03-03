# number = int(input('Enter number:\n'))

# if number%2 == 0:
#     print('it is even')
# else:
#     print('it is odd')


# 2,3,5,7,11

# 4

# 2

#144

# 12

import math

def square_root(num):
    return num ** 0.5

def is_prime():
    number = int(input('Enter number: '))
    if number == 2:
        return 'prime Number'
    if number < 2:
        return 'not prime Number'
    for i in range(2, int(math.sqrt(number) + 2)):
        if number%i == 0:
            return 'not a prime number'
        return 'prime number'

def print_test():
    print('yes')

def print_test_1(): 
    return 'yes'

x = print_test()
y = print_test_1()
print(x,y)
# 0 = 0 (0+0)
# 1 = 1 (1+0)
# 9 = 17 (9 + 8)

for i in range(0, 10):
    if i == 0:
        print('0 sum 0')
    else:
        print(str(i) + ' sum ' + str(i + i-1))

    


