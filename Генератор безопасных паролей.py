import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars = ""

print("Сколько паролей сгенерировать?")
n = int(input())
print("Длина одного пароля?")
length = int(input())
print("Включать ли цифры 0123456789?")
digits_answer = input()
print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
uppercase_letters_answer = input()
print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?")
lowercase_letters_answer = input()
print("Включать ли символы !#$%&*+-=?@^_?")
punctuation_answer = input()
# print("Исключать ли неоднозначные символы il1Lo0O?")
# amb_sym = input()

if uppercase_letters_answer == "1":
    chars = chars + uppercase_letters
if lowercase_letters_answer == "1":
    chars = chars + lowercase_letters
if digits_answer == "1":
    chars = chars + digits
if punctuation_answer == "1":
    chars = chars + punctuation
chars = list(chars)


def generate_password(length, chars):
    for _ in range(n):
        password = "".join(random.sample(chars, length))
        print(password)


generate_password(length, chars)
