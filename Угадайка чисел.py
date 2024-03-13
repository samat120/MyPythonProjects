import random
random_num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
def is_valid(num):
    if 1 <= num <= 100:
        return True
    else:
        return False
result = False
while result == False:
    print('Введите целое число от 1 до 100:')
    num = int(input())
    if is_valid(num) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            result = False
    elif is_valid(num) == True:        
        if num < random_num:
            result = False
            print('Ваше число меньше загаданного, попробуйте еще разок')
        if num > random_num:
            result = False
            print('Ваше число больше загаданного, попробуйте еще разок')
        if num == random_num:
            result = True
            print('Вы угадали, поздравляем!')
            print()
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')