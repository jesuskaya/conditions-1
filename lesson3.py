# обработка исключений

# v1

# n1, n2 = 10, 0
# print(n1 / n2)

# чел вводит з клавы число
# если пользователь ввёл 0 - перестать ввод чисел
# в конце вывести средне ариф. числовую последовательность

sum_nums = 0
count = 0

try:
    while True:
        try:
            number = int(input("Enter any number or 0 for exit: "))

            if number == 0 and count == 0:
            print("please enter another number")
            continue

            if number == 0:
            print("end..")
            break

        sum_nums += number # sum_nums = sum_nums + number
        count += 1
    average = sum_nums / count
    print(f"sum is: {sum_nums}")
    print(f"count: {count}")
    print(f"average is: {average}")
except ValueError as error:
    print("enter number only!")
except Exception as error:
    print(error)