# У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

import random

NUMS_SIZE = 10
sum_min = 0
sum_par = 0
sum_nop = 0
product = 1
prod = 1
sum_full = 0
numbers = []

for i in range(NUMS_SIZE):
    numbers.append(random.randint(-100, 100))

print(numbers)
# 1
for b in range(NUMS_SIZE):
    if numbers[b] < 0:
        sum_min += numbers[b]
# 2
for b in range(NUMS_SIZE):
    if numbers[b] % 2 == 0:
        sum_par += numbers[b]
# 3
for b in range(NUMS_SIZE):
    if numbers[b] % 2 == 1:
        sum_nop += numbers[b]
# 4
for b in range(NUMS_SIZE):
    if b % 3 == 0 and b != 0:
        product *= numbers[b]
# 5
prod = min(numbers) * max(numbers)
# 6
first_positive_index = -1
for b in range(len(numbers)):
    if numbers[b] > 0:
        first_positive_index = b
        break
last_positive_index = -1
for b in range(len(numbers) - 1, -1, -1):
    if numbers[b] > 0:
        last_positive_index = b
        break

if first_positive_index != -1 and last_positive_index != -1 and last_positive_index > first_positive_index:
    for b in range(first_positive_index + 1, last_positive_index):
        sum_full += numbers[b]

print(sum_min)
print(sum_par)
print(sum_nop)
print(product)
print(prod)
print(sum_full)

# Завдання 2
# Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# ■ Створити список цілих, що містить лише парні числа з першого списку;
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.



