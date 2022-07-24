def addition():
    quantity = int(input('Сколько операндов? '))
    total = 0
    for number in range(1, quantity + 1):
        operand = int(input(f'Введите операнд {number} '))
        total += operand
    print(total)


def subtraction():
    quantity = int(input('Сколько операндов? '))
    total = int(input(f'Введите операнд 1 '))
    for number in range(2, quantity + 1):
        operand = int(input(f'Введите операнд {number} '))
        total -= operand
    print(total)


action = input('Выберите операцию: + / -')
if action == '+':
    addition()
if action == '-':
    subtraction()


