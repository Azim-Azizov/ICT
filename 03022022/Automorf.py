while True:
    num = int(input("Enter the number: "))
    stage = num
    check = num ** 2
    num_of_digs = 0
    while stage > 0:
        num_of_digs += 1
        stage //= 10
    if num == check % 10 ** num_of_digs:
        print(f"The square of {num} is {check} and ends with {num}.")
    else:
        print(f"The square of {num} is {check} and does not ends with {num}.")
