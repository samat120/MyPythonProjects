lowercase_letters_en = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string = input()
list = string.split()
list_2 = []

for el in list:
    number_of_letters = 0
    el_string = ""
    word_code = ""
    for sym in el:
        if sym in lowercase_letters_en or sym in uppercase_letters_en:
            number_of_letters += 1
            el_string += sym
            shift = number_of_letters
        else:
            el_string += sym
    for sym in el_string:
        if sym in lowercase_letters_en or sym in uppercase_letters_en:
            letter_lower = sym.lower()
            letter_lower_index = lowercase_letters_en.index(letter_lower)
            if letter_lower_index + shift <= 25:
                code_letter_lower_index = letter_lower_index + shift
            if letter_lower_index + shift >= 26:
                code_letter_lower_index = shift - (26 - letter_lower_index)
            code_letter_lower = lowercase_letters_en[code_letter_lower_index]
            if sym.isupper() == True:
                code_letter = code_letter_lower.upper()
            if sym.islower() == True:
                code_letter = code_letter_lower
            word_code += code_letter
        else:
            word_code += sym
    list_2.append(word_code)
print(" ".join(list_2))
