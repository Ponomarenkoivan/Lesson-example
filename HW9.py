# Написати валідації за допомогою регулярних виразів:
#
# - домашній номер телефону (тільки цифри та довжина номера)
#
# - Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
#
# - email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
#
# - ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)

import re

# home_telephone = ['627654', '468351561', 'nhkb25533', 'nhkb25', '46835156']
# telephone_regex = re.compile(r"^\d{6,8}$")
#
#
# for telephone in home_telephone:
#     if telephone_regex.match(telephone):
#         print(f"telephone: {telephone} is correct")
#     else:
#         print(f"telephone: {telephone} is not correct")
#
# mobile_telephone = ['+380663355777', '+0663355777', '0663355777', '+hkb663355777', '46835156']
# mobile_telephone_regex = re.compile(r"^\+380|\d{10,13}$")
#
#
# for mob_telephone in mobile_telephone:
#     if mobile_telephone_regex.match(mob_telephone):
#         print(f"Mobile telephone: {mob_telephone} is correct")
#     else:
#         print(f"Mobile telephone: {mob_telephone} is not correct")

# email_register = ['helloworld@gmail.com', 'he_loworld@@gmailcom', 'hellowo-rld@gmail.com',
# 'helloworld555@gmail.com', '666helloworld@gmail.com', 'helloworld@gmail.c', 'hellowo&rld@gmail.com']
# email_regex = re.compile(r"^[^\d][\w\.-]{5,50}@gmail\.com$")
#
# for email in email_register:
#     if email_regex.match(email):
#         print(f"Email: {email} is correct")
#     else:
#         print(f"Email: {email} is not correct")

# full_name = ['Ivancheko Petro Petrovich', 'Savcenko Ivan Ivanovich', 'savcenko Ivan ivanovich','s Ivan ivanovichhhhhhhhhhhhhhhh']
# full_name_regex = re.compile(r"^[A-Za-z]{2,20}\s[A-Za-z]{2,20}\s[A-Za-z]{2,20}$")
#
# for name in full_name:
#     if full_name_regex.match(name):
#         print(f"Full name: {name} is correct")
#     else:
#         print(f"Full name: {name} is not correct")