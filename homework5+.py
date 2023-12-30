### Дополнительное задание с матрицами


# import random
#
# matrix = [[random.randint(10, 99) for _ in range(10)] for _ in range(10)]
#
# print("Matrix:")
# for row in matrix:
#     print(row)

# #
# main_diagonal_sum = sum(matrix[i][i] for i in range(10))
# print("Main diagonal sum:", main_diagonal_sum)
#
# #
# secondary_diagonal_values = [matrix[i][9 -i] for i in range(10)]
# min_secondary_diagonal = min(secondary_diagonal_values)
# max_secondary_diagonal = max(secondary_diagonal_values)
# print("Min secondary diagonal: ", min_secondary_diagonal)
# print("Max secondary diagonal: ", max_secondary_diagonal)
#
# #(1)
# column_number = int(input("\nEnter column number(0-9): "))
# column_values = [matrix[i][column_number] for i in range(10)]
# print(f"Column {column_number}: {column_values}")
# #(2)
# row_number = int(input("\nEnter row number(0-9): "))
# row_values = matrix[row_number]
# print(f"Row {row_number}: {row_values}")
#
# #(1)
# swap_column1 = int(input("\nEnter column number(0-9): "))
# swap_column2 = int(input("\nEnter second column number(0-9): "))
#
# for i in range(10):
#     matrix[i][swap_column1], matrix[i][swap_column2] = matrix[i][swap_column2], matrix[i][swap_column1]
# print("\nNew matrix:")
# for row in matrix:
#     print(row)
#(2)
# swap_row = int(input("\nEnter row number (0-9): "))
# swap_row2 = int(input("\nEnter second row number (0-9): "))
#
# temp_row = matrix[swap_row][:]
# matrix[swap_row] = matrix[swap_row2][:]
# matrix[swap_row2] = temp_row
#
# print("\nSwapped matrix:")
# for row in matrix:
#     print(row)

