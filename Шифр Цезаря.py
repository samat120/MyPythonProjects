lowercase_letters_en = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters_ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
uppercase_letters_ru = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

s = input()
print("Выберите направление: шифрование - 1, дешифрование - 2")
direction = int(input())
print("Выберите язык: русский - 1 или английский - 2")
language = int(input())
print("Выберите шаг сдвига:")
shift = int(input())

if direction == 1:
    if language == 1:
        for c in s:
            if c in lowercase_letters_ru or c in uppercase_letters_ru:
                c_lower = c.lower()
                x_index = lowercase_letters_ru.index(c_lower)
                if x_index - shift <= 32:
                    y_index = x_index + shift
                if x_index - shift > 32:
                    y_index = shift - (32 - x_index)
                y_lower = lowercase_letters_ru[y_index]
                if c.isupper() == True:
                    y = y_lower.upper()
                if c.islower() == True:
                    y = y_lower
            else:
                y = c
            print(y, end="")

    if language == 2:
        for c in s:
            if c in lowercase_letters_en or c in uppercase_letters_en:
                c_lower = c.lower()
                x_index = lowercase_letters_en.index(c_lower)
                if x_index - shift <= 26:
                    y_index = x_index + shift
                if x_index - shift > 26:
                    y_index = shift - (26 - x_index)
                y_lower = lowercase_letters_en[y_index]
                if c.isupper() == True:
                    y = y_lower.upper()
                if c.islower() == True:
                    y = y_lower
            else:
                y = c
            print(y, end="")

elif direction == 2:
    if language == 1:
        for c in s:
            if c in lowercase_letters_ru or c in uppercase_letters_ru:
                c_lower = c.lower()
                x_index = lowercase_letters_ru.index(c_lower)
                if x_index - shift >= 0:
                    y_index = x_index - shift
                if x_index - shift < 0:
                    y_index = 32 - (shift - x_index)
                y_lower = lowercase_letters_ru[y_index]
                if c.isupper() == True:
                    y = y_lower.upper()
                if c.islower() == True:
                    y = y_lower
            else:
                y = c
            print(y, end="")

    if language == 2:
        for c in s:
            if c in lowercase_letters_en or c in uppercase_letters_en:
                c_lower = c.lower()
                x_index = lowercase_letters_en.index(c_lower)
                if x_index - shift >= 0:
                    y_index = x_index - shift
                if x_index - shift < 0:
                    y_index = 26 - (shift - x_index)
                y_lower = lowercase_letters_en[y_index]
                if c.isupper() == True:
                    y = y_lower.upper()
                if c.islower() == True:
                    y = y_lower
            else:
                y = c
            print(y, end="")
