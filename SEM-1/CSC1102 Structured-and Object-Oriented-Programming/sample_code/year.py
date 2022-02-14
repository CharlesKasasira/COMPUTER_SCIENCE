# import datetime
import datetime as dt
# from datetime import datetime

date = dt.datetime.today()

print(date.year)
print(date.hour)
print(date.minute)
print(date.second)

print(date.ctime())




# sample code


today = dt.datetime.today()

year = today.year

print('we are in ' +str(year))


# single line comment
# python has no multiple line comments

'''
Documentation in python
these are python docstrings
'''

def get_area(l, w):
    '''
    DocStrings are used after defintion of a function, method and class
    :param l: lenght of a rectangle
    :parm w: width
    :return: area of rectangle
    '''
    return l * w


# functions in python

def greet_user(username):
    greeting = 'hello ' + username
    return greeting



print(greet_user('charles'))



# multiplication program in python

num1 = input('Enter First number \n')
num2 = input('Enter Second Number \n')

multiple = int(num1) * int(num2)

print(multiple)



# Data Structures
list = [1, 2, 3, 4]
tuple = (1, 2, 3, 4)
dictionary = {
    '1': 'one',
    '2': 'two',
    '3': 'three'
}



print('------------------------------')
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))

