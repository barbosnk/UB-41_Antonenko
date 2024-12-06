def find_second_max(max1=None, max2=None):
    num = int(input("Введите натуральное число (или 0 для завершения): "))

    # Если введено 0, значит, конец последовательности
    if num == 0:
        return max2

    # Обновляем max1 и max2 в зависимости от текущего числа
    if max1 is None or num > max1:
        max2 = max1
        max1 = num
    elif max2 is None or (num < max1 and num > max2):
        max2 = num

    # Рекурсивный вызов для следующего числа
    return find_second_max(max1, max2)


# Запуск функции и вывод результата
second_max = find_second_max()
if second_max is None:
    print("Второй по величине элемент не найден.")
else:
    print("Второй по величине элемент:", second_max)