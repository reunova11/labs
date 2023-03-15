def n1():
    delimoe = int(input('Введите делимое '))
    chasn = delimoe % 3
    if chasn == 0:
        print('Число делитcя на 3 без остатка')
    elif delimoe == 0:
        print('Введите корректное число')
    else:
        print('Число делитcя на 3 без остатка')
n1()
def n2():
    try:
        delitel = int(input('Введите делитель '))
        chasn = 100 / delitel
    except ZeroDivisionError:
        print('Введено некорректное число')
    except ValueError:
        print('Введено не число')
    else:
        print('Частным от деления на 100 является ', chasn)
n2()
def n3():
    date = input('Введите дату в формате дд/мм/гггг ')
    date = date.split('/')
    # разделение даты
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print('True')
    else:
        print('False')
n3()
def n4():
    ticket = input('Введите номер билета: ')
    sum1 = 0
    sum2 = 0
    if len(ticket) % 2 == 0:
    # проверяем четное ли кол-во цифр
        for i in ticket[0:int(len(ticket) / 2)]:
            sum1 = sum1 + int(i)
        for i in ticket[int(len(ticket) / 2):int(len(ticket)) + 1]:
            sum2 = sum2 + int(i)
        if sum1 == sum2:
            print('Билет - счастливый')
        else:
            print('Билет не является счастливым')
    else:
        print('Количество цифр нечётно')
n4()
