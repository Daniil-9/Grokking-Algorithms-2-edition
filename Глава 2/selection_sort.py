# Функция для поиска наименьшего элемента массива

def findsmallest(arr):
    smallest = arr[0] # для хранения наименьшего значения
    smallest_index = 0 # для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Встроенные функции

# Для значения: min(arr)
# Для индекса: arr.index(min(arr))

# Функция сортировки выбором

def delectionSort(arr): # сортируем массив
    newArr = []
    copiedArr = list(arr) # копируем массив перед изменением
    for i in range(len(copiedArr)):
        smallest = findsmallest(copiedArr)  # находим мин и добавляем в новый массив
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(delectionSort([5, 3, 6, 2, 10]))