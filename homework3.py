#### Task1

# print("Choose ur day of the week!(1-7)")
# user_select = int(input("Days of the week: "))
# match user_select:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")

#### Task2

# try:
#     print("Choose two numbers:")
#     num1 = float(input("Number 1:"))
#     num2 = float(input("Number 2:"))
#     if num1 != num2:
#         if num1 < num2:
#             print(f"{num2},{num1}")
#         else:
#             print(f"{num1},{num2}")
#     else:
#         print("Numbers is equals")
# except ValueError as error:
#     print(error)
# except Exception as error:
#     print(error)
#
# print("Working next")

#### Task3

# try:
#     print("Choose two numbers:")
#     num1 = int(input("Number 1:"))
#     num2 = int(input("Number 2:"))
#     print("Choose ur operation(+, -, *, /): ")
#
#     Operation = input("Choose: ")
#
#     if Operation == "+":
#         print(num1 + num2)
#     elif(Operation == "-"):
#         print(num1 - num2)
#     elif(Operation == "*"):
#         print(num1*num2)
#     elif(Operation == "/"):
#         if num1 == 0 or num2 == 0:
#             raise ValueError("cant divide by zero")
#         else:
#             print(num1/num2)
# except ValueError as error:
#     print("Print numbers only")
# except Exception as error:
#     print(error)