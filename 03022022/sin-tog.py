x, y = map(int, input("Enter range separated by space: ").split(" "))
num_count = y - x + 1
if num_count % 2 == 0:
    print(f"equals and both are {int(num_count / 2)}")
else:
    single = int((num_count - 1) / 2)
    toggle = single + 1 
    if x % 2 == 0:
        print(f"single numbers equal to {single} and toggle numbers equal to {toggle}")
    else:
        print(f"single numbers equal to {toggle} and toggle numbers equal to {single}")
