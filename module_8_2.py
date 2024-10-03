
def personal_sum(*numbers):
    """среднее арифметическое всех чисел"""
    result = 0 # сумма всех чисел (первоначально равно 0)
    incorrect_data = 0 # количество некорректных данных (первоначально равно 0)
    for i in numbers: # перебор всех чисел в numbers

        for j in i:

            try:
                result += j # суммирование в результат
            except TypeError: # исключение на некорректные данные
                incorrect_data += 1 # суммирование не корректных данных
                print(f'некорректный тип данных для подсчета суммы - {j}') # вывод ошибки
    return result, incorrect_data # возврат результата суммы все чисел, количество некорректных данных


def calculate_average(*numbers):
    """Среднее арифметическое - сумма всех данных делённая на их количество"""
    if isinstance(*numbers, int): # проверка на корректные данные (numbers - целое число)
        return None
    try:
        tuple_pers_sum = personal_sum(*numbers)

        return tuple_pers_sum[0] / (len(*numbers) - tuple_pers_sum[1])
    except ZeroDivisionError: # исключение (деление на 0)
        return 0
    except TypeError: # исключение на некорректные данные
        return (f'В numbers записан некорректный тип данных') #


# Вывод результата
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
