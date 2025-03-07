from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)
text = ('Число меньше или равно нулю')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет положительное ли число и производит необходимые вычисления."""
    if your_number <= 0:
        return text

    x = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {x}')
    return x

    # f'Это будет: {calculate_square_root(your_number)}')


calc(25.5)
