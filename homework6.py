# #### Task 1
#
# def calculate_product(lst):
#     product = 1
#     for element in list:
#         product *= element
#     return product
#
# numbers = [2, 3, 5, 7]
# result = calculate_product(numbers)
# print("Product of the numbers is: ", result)


#### Task 2

# def find_min(numbers):
#     minimum = min(numbers)
#     return minimum
#
# number_list = [0,1,2,3,4,5,6,7,8,9]
# result = find_min(number_list)
# print("Minimum is", result)


#### Task 3

# import random
#
# numbers = [random.randint(-10, 40) for _ in range(10)]
#
# print(numbers)
#
# def is_simple(number: int) -> bool:
#     if number <2:
#         return False
#
#     for num in range(2, number):
#         if number % num == 0:
#             return False
#
#     return True
#
#
# def get_simple_numbers_from_list(nums: list[int]) -> None:
#     for num in nums:
#         if is_simple(num):
#             print(num, end=' ')
#
#     print()
#
# get_simple_numbers_from_list(numbers)


### Task 4

# import random
#
#
# def remove_numbers(lst, number):
#
#     count_removed = lst.count(number)
#     lst[:] = [elem for elem in lst if elem != number]
#     return count_removed
#
#
# my_list = [random.randint(1,5) for _ in range(10)]
# print(my_list)
#
#
# number_to_remove = 3
# removed_count = remove_numbers(my_list, number_to_remove)
#
# print(f"Deleted elements: {removed_count}")
# print(f"List after del: {my_list}")


### Task 5

# import random
#
# def merge_list(list1, list2):
#     merged_list = list1 + list2
#     return merged_list
#
# list1 = [random.randint(1, 5) for _ in range(10)]
# print(list1)
# list2 = [random.randint(1, 5) for _ in range(10)]
# print(list2)
#
# result = merge_list(list1, list2)
# print(result)


### Task 6

# import random
#
#
# def calculate_list(lst, exponent):
#     new_list = [element ** exponent for element in lst]
#     return new_list
#
#
# number_list = [random.randint(1, 5) for _ in range(5)]
# print(number_list)
#
# exponent_value = 2
#
# result = calculate_list(number_list, exponent_value)
# print(result)


sdad





