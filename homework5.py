#### Task_1

# import random
#
# random_numbers = [random.randint(-10, 10) for _ in range(10)]
# print("List:", random_numbers)
#
# #1
# negative_sum = sum(x for x in random_numbers if x < 0)
# print("Negative sum:", negative_sum)
#
# #2
# paired_numbers = sum(x for x in random_numbers if x % 2 == 0)
# print("Paired numbers:", paired_numbers)
#
# #3
# not_paired_numbers = sum(x for x in random_numbers if x % 2 != 0)
# print("Not paired numbers:", not_paired_numbers)
#
# #4 здесь не уверен так ли это нужно было делать
# multiple_of_3 = 1
# multiple_of_3 *= [random_numbers[i] for i in range(0, len(random_numbers), 3)]
# print("Multiple of 3:", multiple_of_3)
#
# #5
# min_index, max_index = random_numbers.index(min(random_numbers)), random_numbers.index(max(random_numbers))
# for_mult = 1
# for_mult *= [random_numbers[i] for i in range(min(min_index, max_index) + 1, max(max_index, min_index))]
# print("Product: ", for_mult)
#
# #6
# positive_indices = [i for i, x in enumerate(random_numbers) if x > 0]
# sum_of_numbers = sum(
#     random_numbers[i] for i in range(positive_indices[0] + 1, positive_indices[-1])
#     if len(positive_indices) >= 2
# )
# print("Sum of numbers:", sum_of_numbers)


#### Task_2

# import random
#
# input_list = [random.randint(-10,10) for _ in range(10)]
# print(input_list)
#
# paired_numbers = [x for x in input_list if x % 2 == 0]
#
# not_paired_numbers = [x for x in input_list if x % 2 != 0]
#
# negative_numbers = [x for x in input_list if x < 0]
#
# positive_numbers = [x for x in input_list if x > 0]
#
# print("Paired numbers: ", paired_numbers)
# print("Not paired numbers: ", not_paired_numbers)
# print("Negative numbers: ", negative_numbers)
# print("Positive numbers: ", positive_numbers)
