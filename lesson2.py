# hello!

# # Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел.
# # Результат вычислений вывести на экран.
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# print(num1 * num2 * num3)
#
# #  Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей.
# first = int(input("Enter first diagonal: "))
# second = int(input("Enter second diagonal: "))
#
# result = first * second / 2
#
# print(result)
#
# # Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр.
# #
# # Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24.
#
# number = int(input("Enter 4-digit number: "))
# #
# # # 4697
# n1 = number // 1000
# n2 = number // 100 % 10
#

# print("Hello world!")

#####
# умови
# v1
# n1 = 10
# n2 = 20
# v2
# n1, n2 = 10, 20  # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)  # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2)  # поверне True якщо обидва операнди різні
# #
# print(1 == 1 and 3 == 3)  # поверне True якщо обидва операнди рівні True, інакше False
# print(1 == 1 or 2 == 3)  # поверне True якщо хоча б один операнд дорівнює True, інакше False
# #
# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки
#
# print("hello" in "hello world")

############
# hours = int(input("Enter hours: "))
#
# if 12 <= hours < 24:
#     print("PM")
# elif 0 <= hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours!")

# ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано

###
# film_rating = int(input("Enter film rating: "))
#
# if film_rating > 0 and film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK!")
#     else:
#         print("Not OK!")
# else:
#     print("Incorrect rating!")
#
# print("Hello world!")

# 1. create develop branch from master branch
# 2. create feature branch from develop branch
# 3.

###
# ввести з клавіатури 3 числа
# - вивести найменше із трьох чисел
# - количество однакових чисел

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))


# вывести наименьшее из трех чисел
if n1 < n2 < n3:
    print(n1)
elif n2 < n3 < n1:
    print(n2)
elif n3 < n2 < n1:
    print(n3)
else:
    print("All numbers equals")
#
# ########
#
# # - кол-во одинаковых чисел
# if n1 == n2 == n3:
#     print(3)
# elif n1 == n2 or n2 == n3 or n1 == n3:
#     print(2)
# else:
#     print(0)
