# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.

# def my_pow(number: int, stepen: int) -> int:
#     if stepen == 0:
#         return 1
#
#     if stepen == 1:
#         return number
#
#     return number * my_pow(number, stepen - 1)
#
#
# try:
#     print(my_pow(6, 4))
# except Exception as error:
#     print(error)
# my_pow(6, 4) -> 6 * my_pow(6, 3) => 1296
# my_pow(6, 3) -> 6 * my_pow(6, 2) => 216
# my_pow(6, 2) -> 6 * my_pow(6, 1) => 36
# my_pow(6, 1) => 6

# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)

# def stars(mage):
#     if mage > 0:
#         print('*', end=' ')
#         stars(mage - 1)
#
#
# numbers_sarts = int(input("Stars: "))
# stars(numbers_sarts)
# stars(4) -> 4 => ****
# stars(3) -> 3 => ***
# stars(2) -> 2 => **
# stars(1) -> 1 => *
# stars(1) =>

#Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

# def long_suma(a, b):
#     if a == b:
#         return a
#     if a > b:
#         return "Pls enter a < b"
#     return a + long_suma(a + 1, b)
#
#
# first_number = int(input("Enter a: "))
# second_number = int(input("Enter b: "))
# print(long_suma(first_number, second_number))

# long_suma(2, 6) -> 2 + long_suma(3, 6) => 20
# long_suma(3, 6) -> 3 + long_suma(4, 6) => 18
# long_suma(4, 6) -> 4 + long_suma(5, 6) => 15
# long_suma(5, 6) -> 5 + long_suma(5, 6) => 11
# long_suma(6, 6) => 6

