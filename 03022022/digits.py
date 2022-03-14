string = input("Which script do you want to use?\n\n1 - single\n2 - double")
if string == "2":
    num = int(input("Enter the number you want to check: "))
    if num < 10:
        print("The number is less than 1.")
    digit = int(num // 10 % 10)
    while num >= 10:
        digit_c = int(num // 10 % 10)
        if digit != digit_c:
            print("The number does not follow the given rle.")
            break
        num //= 100
        if num < 10:
            print("The number follows the given rule.")
elif string == "1":
    num = int(input("Enter the number you want to check: "))
    if num < 1:
        print("The number is less than 1.")
    digit = int(num % 10)
    while num >= 1:
        digit_c = int(num % 10)
        if digit != digit_c:
            print("The number does not follow the given rle.")
            break
        num //= 100
        if num < 1:
            print("The number follows the given rule.")
else:
    print("Enter correct option!")
