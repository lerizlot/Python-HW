import math

# Задача №1
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input('Расстояние в день: '))
m = 750
# m = int(input('Расстояние: '))

result1 = (m + (n - 1)) // n 
result2 = -(-m // n) # целочисленный оператор всегда округляет в меньшую сторону
print(result1, result2)

# Задача №3
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

classA = int(input('В классе A: '))
classB = int(input('В классе B: '))
classC = int(input('В классе C: '))

result = -(-classA // 2 + -classB // 2 + -classC // 2)
result = (classA // 2) + (classB // 2) + (classC // 2) + (classA % 2) + (classB % 2) + (classC % 2)

print(round(classA / 2 + classB / 2 + classC / 2))

print(result)
print(result)

print(f"Нужно {math.ceil(classA/2) + math.ceil(classB/2) + math.ceil(classC/2)} парт")

# Задача №5
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

# Input: 3 4(ввод на разных строках)
# Output: 6

# Задача №7
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# Input: 2016
# Output: YES

natNumber = int(input("Введите натуральное число: "))

# 1-й вариант
if ((natNumber % 4 == 0) and (natNumber % 100 != 0)) or (natNumber % 400 == 0):
    print("Год является высокостным")
else:
    print("Год не является высокостным")

# 2-й вариант
if natNumber % 400 == 0:
    print("Yes")
elif (natNumber % 4 == 0 and natNumber % 100 != 0):
    print("Yes")
else:
    print("No")

# пример
if False and True and True:
    print("Yes")
else:
    print("No")