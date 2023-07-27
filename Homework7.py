# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

def multiplication_numbers(text):
    multiplication = 1
    for numbers in text:
        multiplication *= numbers
    return multiplication


my_text = [10, 5, 6, 8, 6, 3, 7, 8]
print(my_text)
multiplication_results = multiplication_numbers(my_text)
print(multiplication_results)


# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

def minimum_numbers(text1):
    return min(text1)


min_numbers = minimum_numbers(my_text)
print(min_numbers)


# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається із функції.

def simple_numbers(text2):
    for number in text2:
        if text2.count(number) == 1:
            print(number)


simple_numbers(my_text)


# Завдання 4 Напишіть функцію, яка видаляє зі списку ціле задане число. З функції потрібно повернути кількість
# видаленних елементів.

def integer(text3, number1):
    number_of_deletions = text3.count(number1)
    for i in range(number_of_deletions):
        text3.remove(number1)
    return number_of_deletions


times = integer(my_text, 3)
print(times)


# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків

def two_lists(text4, text5):
    combined_list = text4 + text5
    return combined_list


lists1 = [1, 5, 8, 9, 0, 9, 5, 3]
lists2 = [3, 11, 7, 10, 0, 9, 4, 1]

lists3 = two_lists(lists1, lists2)
print(lists3)

# Завдання 6 Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих. Значення для ступеня передається
# як параметр, список також передається як параметр. Функція повертає новий список, який містить отримані результати.

def raise_to_a_degree(text5, degree):
    for i in range(len(text5)):
        text5[i] = text5[i] ** degree


lists5 = [1, 5, 8, 9, 3, 9, 5, 3]
degree = 2
raise_to_a_degree(lists5, degree)
print(lists5)
