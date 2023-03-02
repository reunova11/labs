nom = int(input('Введите номер вашего места '))
print()
if nom >= 36:
    print('У вас боковое место')
elif nom % 2:
    print('У вас нижнее место')
else:
    print('У вас верхнее место')
