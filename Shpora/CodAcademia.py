numbers = list(range(3,5))
print(numbers)



number = 10
number += 5
print(number)


# number1 = list(3,4)
# print(number1)

user = ("Tom", 23)
print(user)



users = {0: "Tom", 2: "Bob", 3: "Bill"}
print(users[0])


# '''Выводит тип переменной'''
user_id = 234
print(type(user_id))



# '''len Выводит колличество символов в переменной!'''
string = "12344556hrk        gkgkwkg"
string_number = len(string)
print(string_number)

parrot = "Norwegian Blue"
print(len(parrot))


# '''Делает все символы строчные'''
parrot = "Norwegian 2#3 Blue"
print(parrot.lower())


# '''Все символы заглавные'''
parrot = "Norwegian Blue"
print(parrot.upper())


# Конкантенация(склеивание) текста """
print('Spam ' + 'and ' + 'eggs')


# Преобразование в строку
eggs = 2
print('i ' + 'have ' + str(eggs) + ' eggs')


# Объеденение строки с переменной
eggs = 'Opp'
name = "Mike"
print("Hello %s %s" % (name, eggs))

day = 6
print("03 - %s - 2019" % (day))
# 03 - 6 - 2019
print("03 - %02d - 2019" % (day))
# 03 - 06 - 2019


# name = input("What is your name? ")
# quest = input("What is your quest? ")
# color = input("What is your favorite color? ")
#
# print("Ah, so your name is %s, your quest is %s, " \
# "and your favorite color is %s." % (name, quest, color))


my_string = 'Я буду кодером'
print(len(my_string))
print(my_string.upper())


'''Выводит максимальное число "max" '''
maximum = max(123, 111, 5, -45, 0)
print(maximum)

'''Выводит минимальное число "min" '''
minimum = min(123, 111, 5, -45, 0)
print(minimum)

'''Выводит колличество шагов до нуля "abs" '''
absolute = abs(-5)
print(absolute)



