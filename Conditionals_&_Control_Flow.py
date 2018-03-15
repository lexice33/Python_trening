# Равно Возвращает True/False
2 == 2

# Не равно
2 != 5

# Меньше/ больше или равно
print(5 > 2)
2 < 5
5 >= 2
2 <= 5
print(99 != (98 + 1))


# Булевые операторы
'''and - который проверяет, имеются ли оба утверждения True;
or - который проверяет, есть ли хотя бы одно из утверждений True;
not - что дает противоположное утверждение.'''

print(True and False)
print(3 ** 4)


answer = "'Tis but a scratch"


def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


# print(greater_less_equal_5(4))
# print(greater_less_equal_5(5))
# print(greater_less_equal_5(6))


# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90 :
        return "A"
    elif grade >= 80 and grade <= 89:
         return "C"
    elif grade >= 70 and grade <= 72:
         return "D"
    else:
        return "F"


# This should print an "A"
print(grade_converter(90))

# This should print a "C"
print(grade_converter(80))

# This should print an "F"
print(grade_converter(61))