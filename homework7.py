# Task_1
import re
#
#
# phone_numbers = ["380991652934", "380991652935", "380991"]
# print(phone_numbers)
#
# for number in phone_numbers:
#     if re.match(r"\d{7}", number):
#         print(f"Number {number} valid")
#     else:
#         print(f"Number {number} invalid")

# Task_2
#
# phone_numbers = ["+91123456789", "3806789012345", "+38096890123456"]
# print(phone_numbers)
# for number in phone_numbers:
#     if re.match(r"\+?\d{12}", number): # помню что лучше добавить ^, $.
#         print(f"Number {number} invalid")
#         print(f"Number {number} Valid")
#     else:


# Task_3
#
# emails = ["ggsgge@mailru", "microsoft.user@gmail.com", "ursasss@outlook.com"]
#
# for email in emails:
#     if re.match(r"^[a-zA-Z]+[._]?[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}$", email):
#         print(f"Email: {email} valid")
#     else:
#         print(f"Email: {email} is not valid")

# Task_4

# fio = "tom Michael Soyer"
#
# if re.match(r"^[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}\s[A-Z][a-z]{1,19}$", fio):
#     print("Correct")
# else:
#     print("Incorrect")

# Task_5(additionally)

# password = "Myname123!"
# ur_password = input("Enter your password(8-16):") # добавил функцию ввода, посмотреть для себя, будет ли работать.
# password = ur_password
# if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$", password):
#     print("Awesome")
# else:
#     print("Bad password")