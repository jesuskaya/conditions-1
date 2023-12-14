#Task - 1

# f1 = int(input("Enter a number 1: "))
# f2 = int(input("Enter a number 2: "))
# f3 = int(input("Enter a number 3: "))
#
# print("Choose operation")
# print("1 - max")
# print("2 - min")
# print("3 - average")
#
# choice = int(input("Enter your choice: "))
#
# if choice == 1:
#     result1 = max(f1, f2, f3)
#     print("The maximum is:", {result1})
# elif choice == 2:
#     result2 = min(f1, f2, f3)
#     print("The minimum is:", {result2})
# elif choice == 3:
#     result3 = (f1 + f2 + f3) / 3
#     print("The average is:", {result3})
# else: print("Invalid!")

#Task 2

meters = float(input("Enter the meters: "))

print("Choose operation")
print("1 - yards")
print("2 - miles")
print("3 - inches")

choice = input("Operation:")

yards = 0.9144
miles = 1609.34
inches = 0.0254

if choice == "1":
    result = meters / yards
    print("The result is:", result)
elif choice == "2":
    result = meters / miles
    print("The result is:", result)

elif choice == "3":
    result = meters / inches
    print("The result is:", result)
else: print("Invalid")


