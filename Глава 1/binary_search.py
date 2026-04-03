def binary_search(arr, item):
    low = 0                 # Нижняя граница списка
    high = len(arr) - 1     # Верхняя граница списка

    while low <= high:              # Пока эта часть не сократится до одного элемента...
        mid = (low + high) // 2     # ...проверяем средний элемент
        guess = arr[mid]
        if guess == item:    # Значение найдено
            return mid
        elif guess > item:   # Много
            high = mid - 1
        else:                # Мало
            low = mid + 1
    return None          # Значения не существует

 my_list = [1, 3, 5, 7, 9]   # Протестируем

print(binary_search(my_list, 3)) # => 1       Нумерация начинается с 0
print(binary_search(my_list, -1))  # => None       В Python None означает "ничто", те элемент не найден
