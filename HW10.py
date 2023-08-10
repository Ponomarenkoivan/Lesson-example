# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу всі слова, що складаються не менше ніж з семи літер.
#
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

with open('text.txt', 'r', encoding='utf-8') as f1:
    content = f1.read()

words = content.split()

with open('newfile', 'w', encoding='utf-8') as f2:
    for word in words:
        if len(word) >= 7:
            f2.write(word + '\n')


word_count = len(words)

print(f"Кількість слів: {word_count}")
