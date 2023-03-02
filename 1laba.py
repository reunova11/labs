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
    elif char in "@#$%&*^~":
        is_spec = True
if len(pas) > 4 and is_numeric and is_spec and is_lower and is_upper:
    print('Пароль надежный')
else:
    print('Пароль ненадежный')