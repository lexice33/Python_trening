# names = ["Adam","Alex","Mariah","Martine","Columbus"]
# for x in names:
#     print(x)


# webster = {
#   "Aardvark" : "A star of a popular children's cartoon show.",
#   "Baa" : "The sound a goat makes.",
#   "Carpet": "Goes on the floor.",
#   "Dab": "A small amount."
# }
#
# for key in webster:  #Выводит все значения
#     print(webster[key])
#
#
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for number in a: #Выводит все четные цифры
#     if number % 2 == 0:
#         print(number)

# def count_small(numbers):
#   total = 0
#   for n in numbers: # Считаеи цифры < 10
#     if n < 10:
#       total = total + 1
#   return total
#
# lotto = [4, 8, 15, 16, 23, 42]
# small = count_small(lotto)
# print(small)


#
# def fizz_count(x):
#     count = 0
#     for item in x: # Считает фразы "fizz"
#         if item == "fizz":
#             count = count + 1
#     return count
#
# aaa = ["fiz", "c", "dog", "fizz", "fizz"]
# bbb = fizz_count(aaa)
# print(bbb)

for letter in "Codecademy":
    print(letter)

# Empty lines to make the output pretty
print()
print()

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print(letter)