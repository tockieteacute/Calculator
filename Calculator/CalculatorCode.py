# функция для вычисления выражения
def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Ошибка вычисления"

# получаем выражение от пользователя
expression = input("Введите математическое выражение: ")

# выводим результат вычисления
print(calculate(expression))