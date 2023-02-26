import random


def get_lenght_list() -> int:
    value: str = input('Введите желаемую длину списка: ')
    try:
        lenght_list: int = int(value)
        if lenght_list < 0:
            print('Значение должно быть положительным числом.')
            lenght_list = get_lenght_list()
    except ValueError:
        print('Значение не может быть использовано!')
        lenght_list = get_lenght_list()
    return lenght_list


def fill_list(lenght_list: int) -> list[int]:
    numbers_list: list[int] = [random.randint(0, 100) for i in range(lenght_list)]
    print('\nСгенерированный список:', *numbers_list, sep=', ')
    return numbers_list


def selection_sort(numbers_list: list[int]):
    print('\n*Сортировка выбором*')
    for current_index in range(len(numbers_list) - 1):
        position: int = current_index
        for i in range(current_index + 1, len(numbers_list)):
            if numbers_list[i] < numbers_list[position]:
                position = i
        if position != current_index:
            numbers_list[current_index], numbers_list[position] = numbers_list[position], numbers_list[current_index]
        print(f'{current_index + 1}-я итерация', *numbers_list, sep=', ')


def sort_bubble(numbers_list: list[int]):
    print('\n*Сортировка пузырьком*')
    for current_index in range(len(numbers_list) - 1):
        for i in range(len(numbers_list) - 1):
            if numbers_list[i] > numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
        print(f'{current_index + 1}-я итерация', *numbers_list, sep=', ')


def sort_bubble_optimize(numbers_list: list[int]):
    print('\n*Сортировка пузырьком*')
    for current_index in range(len(numbers_list) - 1):
        for i in range(len(numbers_list) - 1 - current_index):
            if numbers_list[i] > numbers_list[i + 1]:
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
        print(f'{current_index + 1}-я итерация', *numbers_list, sep=', ')


user_lenght_list = get_lenght_list()
test_list1 = fill_list(user_lenght_list)
selection_sort(test_list1)

test_list2 = fill_list(user_lenght_list)
sort_bubble_optimize(test_list2)