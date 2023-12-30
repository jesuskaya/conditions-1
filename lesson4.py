#lesson 4

# for i in range(5): # от 0 до 4
#     print(i, end=" ")
# print()

#

# for i in range(2, 5):
#     # print("hello")
#     print(i, end=" ")
#
# print()

#

# for i in range(1, 5, 2):
#     # print("hello")
#     print(i, end=" ")
# print()

#

# start, end = 1, 10
# for i in range(start, end+1):
#     print(i, end=" ")
# print()
#
# start, end = 1,10
# for i in range(end, start - 1, -1):
#     print(i, end=" ")


###
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print()
#
# print()
# ##
#
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i * j, end=" ")
#         j += 1
#     print()
#     i += 1

#####
# try:
#
#     start = int(input("Enter start value: "))
#     end = int(input("Enter end value: "))
#
#     if start > end:
#         start, end = end, start
#
#         for number in range(start, end+1):
#             if number < 2:
#                 continue
#
#             is_simple = True
#
#             for i in range(2, number):
#                 if number % i == 0:
#                     is_simple = False
#                     break
#             if is_simple:
#                 print(number, end=" ")
#
#
# except Exception as error:
#     print(error)

# message = "hello world"
# message_1 = 'hello world'
# print(message)

##

text = ("allo"
        " ge")
print(text)