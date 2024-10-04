def personal_sum(numbers):
    result = 0  # сумма всех чисел (первоначально равно 0)
    incorrect_data = 0  # количество некорректных данных (первоначально равно 0)
    for i in numbers:  # перебор всех чисел в numbers
        try:
            result += i  # суммирование в результат
        except TypeError:  # исключение на некорректные данные
            incorrect_data += 1  # суммирование не корректных данных
            print(f'Некорректный тип данных для подсчета суммы - {i}')  # вывод ошибки
    return (result, incorrect_data)  # возврат результата суммы всех чисел, количество некорректных данных

def calculate_average(numbers):
    try:
        per_sum = personal_sum(numbers) # обращение к функции personal_sum
        average_sum = per_sum[0] / (len(numbers) - per_sum[1]) # вычисление среднегоарифметического
        return average_sum
    except ZeroDivisionError: # исключение (деление на 0)
        return 0
    except TypeError:  # исключение на некорректные данные
        print('В numbers записан некорректный тип данных') #вывод ошибки
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')