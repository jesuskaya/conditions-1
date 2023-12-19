try:
    print("Choose two numbers:")
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    if num1 != num2:
        if num1 < num2:
            print(f"{num2},{num1}")
        else:
            print(f"{num1},{num2}")
    else:
        print("Numbers is equals")
except ValueError as error:
    print(error)

print("Working next")