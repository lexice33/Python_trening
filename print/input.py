# # Проверяем что строка не пустая len
# original = input("Введите слово: ")
# if len(original) > 0:
#     print(original)
# else:
#     print("empty")
#
#
# # Проверка на наличие в строке букв  isalpha == True, если не только == FAlse
#
# original = input("Enter: ")
# if len(original) > 0 and original.isalpha():
#     print(original)
# else:
#     print("empty")


pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
    print('empty!')