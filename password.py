password = input('Введите пароль: ')

try:
    answer1 = 10 / len(password)
    answer2 = int(password)
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')
except ValueError:
    print('Требования к паролю не соблюдены')
