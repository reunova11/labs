b = ''
a = ''
while a != '.':
    a = input('введите слово: ')
    b += a + ' '
print('ваше предложение:' , b)

def p1():

    words = []
    while (new_word := str(input())) != "stop":
        words.append(new_word)
    print(" ".join(words))
p1()
def p2():
 words = []
 while (new_word := str(input())) != "stop":
     if "ф" in new_word or "Ф" in new_word:
            print("Ого! Это редкое слово!")
     else:
            print("Эх, это не очень редкое слово...")
p2()
from random import randint
def p3():
    n = 0
    p = 0
    while n < 3:
        a = randint(1, 50)
        b = randint(1, 50)
        print(f"{a} + {b} = ", end="")
        otv = input()
        if not otv.isdigit() and otv != "stop":
            print("Некорректный ввод, повторите попытку!")
            otv = input()
            if (a + b) != int(otv):
                print("Ответ неверный:(")
                n += 1
            if (a + b) == int(otv):
                print("Правильно!")
                p += 1
            if n >= 3:
                print("Игра окончена. Правильных ответов: ", p)
        elif otv == "stop":
            print("Игра завершена.")
        else:
            if (a + b) != int(otv):
                print("Ответ неверный:(")
                n += 1
            if (a + b) == int(otv):
                print("Правильно!")
                p += 1
            if n >= 3:
                print("Игра окончена. Правильных ответов: ", p)
p3()

