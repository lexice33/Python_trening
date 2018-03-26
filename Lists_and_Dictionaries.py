"""".append" добавляет элемент в конец списка"""
suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("lamp")
suitcase.append("box")
suitcase.append("bathing suit")

list_length = len(suitcase) # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)


"""Выводим часть списка"""
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
# The first and second items (index zero and one)
first = suitcase[0:2]
# Third and fourth items (index two and three)
middle = suitcase[2:4]
# The last two items (index four and five)
last =  suitcase[4:]

"""Режем списки"""

animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

"""Определяем индекс элемента"""
animals = ["ant", "bat", "cat"]
print(animals.index("bat")) # 1


"""Вставляем элемент в список и смещаем все элементы находящиеся
в списке"""
animals.insert(1, "dog")
print(animals) #['ant', 'dog', 'bat', 'cat']


animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")
print(duck_index) # 2
animals.insert(duck_index, "cobra")
print(animals) #"aardvark", "badger", "cobra", "emu", "fennec fox"

"""Изменяем циклом каждый элемент в списке"""
my_list = [1,9,3,8,5,7]

for number in my_list:
    print(number * 2)


"""Сортировка списка sort"""
start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
     square_list.append(x ** 2) #[25, 9, 1, 4, 16]
square_list.sort() #[1, 4, 9, 16, 25]

print("!!!")
print(square_list)

"""DICTIONARY"""
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print(residents['Sloth']) # Prints Puffin's room number

