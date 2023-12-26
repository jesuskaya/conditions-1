isalpha(): повертає True, якщо рядок складається лише з алфавітних символів

print(text.isalpha())

# islower(): повертає True, якщо рядок складається лише із символів у нижньому регістрі

print(text.islower())

# isupper(): повертає True, якщо всі символи рядка у верхньому регістрі

print(text.isupper())

# isdigit(): повертає True, якщо всі символи рядка - цифри

print(text.isdigit())

# isnumeric(): повертає True, якщо рядок є числом

print(text.isnumeric())

# startswith(str): повертає True, якщо рядок починається з підрядка str

print(text.startswith("helLo"))

# endswith(str): повертає True, якщо рядок закінчується на підрядок str

print(text.endswith("D"))

# lower(): перекладає рядок у нижній регістр

print(text.lower())

# upper(): перекладає рядок у верхній регістр

print(text.upper())

# title(): початкові символи всіх слів у рядку перекладаються у верхній регістр

print(text.title())

# capitalize(): перекладає у верхній регістр першу літеру тільки першого слова рядка

print(text.capitalize()) # делает так что все предложения начинаются с большой буквы







####

# Заданий рядок
my_string = "Hello, World!"

# Вивести третій символ цього рядка.
print(my_string[2])

# Вивести передостанній символ цього рядка.
print(my_string[-2])

# Вивести перші п'ять символів цього рядка.
print(my_string[:5])

# Вивести весь рядок, крім двох останніх символів.
print(my_string[:-2])

# Вивести усі символи з парними індексами.
print(my_string[::2])

# Вивести усі символи з непарними індексами.
print(my_string[1::2])

# Вивести усі символи у зворотному порядку.
print(my_string[::-1])

# Вивести усі символи рядка через один у зворотному порядку, починаючи з останнього.
print(my_string[-1::-2])

# Вивести довжину цього рядка.
print(len(my_string))
