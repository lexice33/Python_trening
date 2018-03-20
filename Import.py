'''Импорт библиотеки и использование функции'''
# import math
# print(math.sqrt(25))


'''Импорт функции без необходимости указывать библиотеку'''
# from math import sqrt
# print(sqrt(100))

'''Импорт всех функций из либы '''
from math import *
print(sqrt(9))

'''Выводит все функции либы'''
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!