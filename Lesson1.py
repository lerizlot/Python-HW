### Ввод данных из консоли
print('Введите первое число')
a = int(input()) # переводим строку в число
print('Введите второе число')
b = input()
print(a, ' + ', b, ' = ', a + b)
# input() - ввод данных(строка)

# Округление числа
a = 5.58403
b = 8.52470
print(round(a * b, 5))

# Сокращенные операции присваивания (вместо i++)
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5

# Метод флажка (замена break):

# Задача
# Пользователь вводит число, необходимо найти минимальный делитель данного числа

# Решение:
n = int(input())
flag = True
i = 2
while flag:
 if n % i == 0: # если остаток при делении числа n на i равен 0
    flag = False
    print(i)
 elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
    print(n)
    flag = False
    i += 1

# Цикл for, range
# Пример использования цикла for:

# for i in enumeration:
 # operator 1
  # operator 2
  # ...
  # operator n

for i in 1, -2, 3, 15, 5:
    print(i)
 # 1 -2 3 15 5

 # Можно использовать цикл for() и со строками, так как у строк есть нумерация, 
 # такая же как и у массивов, начинается с 0:
 
for i in 'qwerty':
    print(i)
 # q
 # w
 # e
 # r
 # t
 # y

# Цикл for, функция range()
# Range выдает значения из диапазона с шагом 1.
# Если указано только одно число — от 0 до заданного числа.
# Если нужен другой шаг, третьим аргументов можно задать приращение.

r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20
r = range(100, 0, -20) # range(100, 0, -20)

for i in r:
    print(i)
# 100 80 60 40 20

# Вложенный цикл:
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
        print(line)

# Работа со строками
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.lower()) # съешь ещё этих мягких французских булок
print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# Срезы
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # съешь ещё этих мягких французских булок
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...