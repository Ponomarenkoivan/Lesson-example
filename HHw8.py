# Завдання 4.
# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим чином і
# знаходить позицію, з якої починається послідовність із 10 чисел, сума яких мінімальна.

def serch_first_nuber(masiv, position_now=0, min_sum=None, position_min_sum=None):
    if position_now + 10 > len(masiv):
        return position_min_sum

    suma = sum(masiv[position_now:position_now + 10])

    if min_sum is None or suma < min_sum:
        min_sum = suma
        position_min_sum = position_now

    return serch_first_nuber(masiv, position_now + 1, min_sum, position_min_sum)

import random

masiv_numbers = [random.randint(1, 100) for _ in range(100)]
position = serch_first_nuber(masiv_numbers)

print(masiv_numbers)
print("Початкова позиція мінімальної послідовності суми з 10ти:", position)
print("Мінімальна сума:", sum(masiv_numbers[position:position + 10]))
