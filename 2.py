pas = input('Введите пароль ')
is_numeric = False
is_upper = False
is_lower = False
is_spec = False
for char in pas:
    if char.isnumeric():
        is_numeric = True
    elif char.islower():
        is_lower = True
    elif char.isupper():
        is_upper = True
    "@#$%&*^~"  char in "@#$%&*^~":
        is_spec = True
if len(pas) > 4 and is_numeric and is_spec and is_lower and is_upper:
    print('Пароль надежный')
else:
    print('Пароль ненадежный')
def n1():
nom = int(input('Введите номер вашего места '))
print()
if nom >= 36:
    print('У вас боковое место')
elif nom % 2:
    print('У вас нижнее место')
else:
    print('У вас верхнее место')
n1()
def n2():
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Год является високосным')
else:
    print('Год не является високосным')
n2()
def n3():
b = ''
a = ''
while a != '.':
    a = input('введите слово: ')
    b += a + ' '
print('ваше предложение:' , b)
n3()
def n4():
    a = input('Введите цвет: ')
    if (a != "красный") and (a != "синий") and (a != "желтый"):
        print('Ошибка! Введите цвет: красный, синий или желтый')
    b = input('Введите цвет: ')
    if (b != "желтый") and (b != "красный") and (b != "синий"):
        print('Ошибка! Введите цвет: красный, синий или желтый')
    if a == "красный":
        if b == "синий":
            print('Полученный цвет: фиолетовый')
        if b == "желтый":
            print('Полученный цвет: оранжевый')
        if b == "красный":
            print('Полученный цвет: красный')
    if a == "синий":
        if b == "красный":
            print('Полученный цвет: фиолетовый')
        if b == "желтый":
            print('Полученный цвет: зеленый')
        if b == "синий":
            print('Полученный цвет: синий')
    if a == "желтый":
        if b == "красный":
            print('Полученный цвет: оранжевый')
        if b == "желтый":
            print('Полученный цвет: желтый')
        if b == "синий":
            print('Полученный цвет: зеленый')
n4()