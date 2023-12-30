# Функции

# def say_hello():
#     print("Hello World!")
#
# number = 10
# print(number)
# print(say_hello)
# say_hello()
# say_hello()

# def say_hello():
#     print("Hello")
#
#
# number = 10
# print(number)
# print(say_hello)
# say_hello()  # виклик функції (функція починає працювати)
# say_hello()
#
#
# def say_hello():
#     print("Hello Friends!")
#
#
# say_hello()
#
#
# def say_hello(name):
#     print(f"Hello {name}!")
#     name = "qqqq"
#     print(f"Hello {name}!")
#
#
# say_hello("Test user")
# name = "Anton"
# say_hello(name)
# print(name)


# def say_hello_name(username):
#     print(f"Hello, {username}")
#
#
# say_hello_name("Vasya")
# name = "Petya"
# say_hello_name(name)
# #


# def user_info(name: str, age: int, hobby: str) -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     user_hobby = input("Enter your hobby: ")
#     user_info(name, age, user_hobby)
# except Exception as e:
#     print(e)

########
#####################
# після того як відпрацює ключове слово return - функція припиняє свою роботу (тільки функція)
# return – поверне результат роботи функції. Після відпрацьовування return - решта дій функції не відпрацюють
# та функція завершить свою роботу. Якщо у функції є цикл - у циклi return працює як break,
# але на відміну від break – поверне результат, а не просто
# Зупинить дії. Якщо функції є цикли, і в одному з циклів спрацював return - функція припинить свою роботу.
# ключове слово return може зустрічатися в тілі функції скільки завгодно разів
#
# def add(n1, n2):
#     return n1 + n2
#
#
# def sub(n1, n2):
#     return n1 - n2
#
#
# def mult(n1, n2):
#     return n1 * n2
#
#
# def division(n1, n2):
#     return n1 / n2
#
#
# def show_result(num1, num2, math_action, math_func) -> None:
#     print(f"{num1} {math_action} {num2} = {math_func(num1, num2)}")
#
#
# def calculate() -> None:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     math_operation = input("Enter math operation + - * / ")
#
#     match math_operation:
#         case "+":
#             show_result(first_number, second_number, math_operation, add)
#         case "-":
#             show_result(first_number, second_number, math_operation, sub)
#         case "*":
#             show_result(first_number, second_number, math_operation, mult)
#         case "/":
#             show_result(first_number, second_number, math_operation, division)
#         case _:
#             raise Exception("Invalid math operation!")
#
#
# try:
#     calculate()
# except ValueError:
#     print("Enter a valid number!")
# except ZeroDivisionError:
#     print("Do not divide by zero please!")
# except Exception as error:
#     print(error)

###

# def user_info(name: str, age: int = 18, hobby: str = "no hobby") -> None:
#     print(f"Welcome, {name}! Your age: {age} and hobby is {hobby}")
#
#
# # user_info("Vasya", 33, "test")
# # user_info("Vasya", 33)
# # user_info("Vasya")
#
# # user_info("walking", "Petya", 33)
# user_info(hobby="walking", name="Petya", age=33)

#####
# Усі параметри,
# які розташовуються праворуч від символу *, отримують значення лише на ім'я:

# def print_person(name, *, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Bob", age=41, company="Microsoft")
#
#
# def print_person(*, name, age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person(age=41, name="Bob", company="Microsoft")

# Якщо навпаки треба визначити параметри, яким можна передавати значення лише за позицією,
# тобто позиційні параметри, можна використовувати символ /: всі параметри, які йдуть до символу / ,
# є позиційними і можуть отримувати значення лише за позицією

# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Tom", company="JetBrains", age=24)  # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)


# def print_person(name, /, age=18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
#
#
# print_person("Sam", company="Google")  # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company="JetBrains")  # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company="Microsoft", age=42)  # Name: Bob  Age: 42  company: Microsoft

####
# 1. Створити список чисел. Заберіть дублікати значень. Вивести унікальні значення.
# import random
#
#
# def create_list_with_random_numbers(list_length=10, start_number=1, end_number=10) -> list:
#     # v1
#     # new_list = list()
#     # for _ in range(list_length):
#     #     new_list.append(random.randint(start_number, end_number))
#     # return new_list
#
#     # v2
#     return [random.randint(start_number, end_number) for _ in range(list_length)]
#
#
# def remove_duplicates(list_to_remove) -> list:
#     return list(set(list_to_remove))
#
#
# def get_unique_values(list_numbers) -> list:
#     unique_values = []
#     for number in list_numbers:
#         if list_numbers.count(number) == 1:
#             unique_values.append(number)
#
#     return unique_values


# numbers = create_list_with_random_numbers()
# print(numbers)
# numbers_without_duplicates = remove_duplicates(numbers)
# print(numbers_without_duplicates)
# unique_numbers = get_unique_values(numbers)
# print(unique_numbers)

# 2. Дано два списки чисел.
# Порахуйте, скільки чисел міститься як у першому списку, і у другому.

# numbers_1 = create_list_with_random_numbers(start_number=1, end_number=20)
# numbers_2 = create_list_with_random_numbers(start_number=1, end_number=20)
#
# print(numbers_1)
# print(numbers_2)
#
#
# def calc_number_of_equals_numbers_v1(nums_1: list[int], nums_2: list[int]) -> int:
#     print(set(nums_1).intersection(set(nums_2)))
#     return len(set(nums_1).intersection(set(nums_2)))
#
#
# def calc_number_of_equals_numbers_v2(nums_1: list[int], nums_2: list[int]) -> int:
#     def get_number_of_unique_values(first_nums: list[int], second_nums: list[int]) -> int:
#         counter = 0
#         equals_numbers = []
#         for num in first_nums:
#             if num in second_nums and num not in equals_numbers:
#                 equals_numbers.append(num)
#                 counter += 1
#
#         print(equals_numbers)
#         return counter
#
#     if len(nums_1) < len(nums_2):
#         return get_number_of_unique_values(nums_1, nums_2)
#     else:
#         return get_number_of_unique_values(nums_2, nums_1)
#
#
# print(f"Result: {calc_number_of_equals_numbers_v1(numbers_1, numbers_2)}")
# print(f"Result: {calc_number_of_equals_numbers_v2(numbers_1, numbers_2)}")

###########
# 3. Даний текст: у першому рядку записано число рядків, далі йдуть самі рядки.
#
# Визначте, скільки різних слів міститься у цьому тексті.
#
# Словом вважається послідовність непробільних символів, що йдуть поспіль,
# слова розділені одним або більшим числом пробілів або символами кінця рядка.

def generate_text(seed="Hello", multiplier=5):
    return (seed + " ") * multiplier


def calc_diff_strings(text: str) -> int:
    print(text)
    print(text.split())
    return len(set(text.split()))


print(calc_diff_strings(generate_text("Hello world", 10)))
print(calc_diff_strings(generate_text("Hello how are you thank you", 1)))
