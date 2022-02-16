# print('hello world')

# def print_hello():
#     print('hello')

# print_hello()


'''
    You are a Square
'''

'''
checking for a Square number
n = n ** n
'''

from cmath import sqrt
import math
from re import I


def is_square(n):
    if n < 0:
        return False

    sqroot = int(math.sqrt(n))
    if sqroot ** 2 == n:
        return True
    else:
        return False



def is_square2(n):
    if n < 0:
        return False
    sqroot = int(n ** 0.5)
    if sqroot ** 2 == n:
        return True
    else:
        return False


def is_square3(n):
    if n >= 0:
        if int(n ** .5) ** 2 == n:
            return True
    return False

# print(is_square3(36))



def is_square4(n):    
    return n >= 0 and (n**0.5) % 1 == 0




# Python Strings
# print('Python string methods')

# split string
string = 'this is a string'
# print(string.split(' '))


num_string = '6 2 5 4 1'

num_list = num_string.split(' ')

largest_num = int(num_list[0])
for index in range(len(num_list)):
    if int(num_list[index]) > largest_num:
        largest_num = num_list[index]

# print(largest_num) 



def high_and_low(number):
    num_list = number.split(' ')
    high_num = int(num_list[0])
    low_num = int(num_list[0])
    for index in range(len(num_list)):
        if int(num_list[index]) > int(high_num):
            high_num = num_list[index]
        if int(num_list[index]) < int(low_num):
            low_num = num_list[index]

    return f'{high_num} {low_num}'


# print(high_and_low("1 9 3 4 -5"))


def high_and_low2(number):
    nums = sorted(number.split())
    print(f'{nums[-1]} {nums[0]}')



high_and_low2("1 9 3 4 -5")





