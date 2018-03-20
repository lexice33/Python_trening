#
# def tax(bill):
#     """Adds 8% tax to a restaurant bill."""
#     bill *= 1.08
#     print("With tax: %s" % bill)
#     return bill
#
#
# def tip(bill):
#     """Adds 15% tip to a restaurant bill."""
#     bill *= 1.15
#     print("With tip: %s" % bill)
#     return bill
#
#
# meal_cost = 100
# meal_with_tax = tax(meal_cost)
# meal_with_tip = tip(meal_with_tax)
#
# '''Функция может вызывать функцию'''
# def one_good_turn(n):
#     return n + 1
#
# def deserves_another(n):
#     return one_good_turn(n) + 2


def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


x = 9
y = cube(x)
z = by_three(y)
print(y)
print(z)
print(729 ** 3)

print(type(1))
print(type(222.2))
print(type("qwe"))


def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"



from math import sqrt
mat = print(sqrt(13689))

def distance_from_zero(zero):
    if type(zero) == int or type(zero) == float:
        return abs(zero)
    else:
        return "Nope"

print(distance_from_zero(-10))
