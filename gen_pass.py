import random
from string import ascii_lowercase, ascii_uppercase

# создание рандомного пароля
def get_password(length):
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


# проверка на положительность числа
def examination_int(examination):
    while True:
        try:
            value = int(input(examination))
            if value > 0:
                return value
            else:
                print("Введите число больше 0")
        except ValueError:
            print("Неверный формат. Укажите целое число.")


N = examination_int('Введите количество паролей: ')
length = examination_int('Введите длину пароля: ')

for _ in range(N):
    print(get_password(length))



