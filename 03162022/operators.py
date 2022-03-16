import operator


exe = input()
num = ""
nums = []
oper = ""
for i in exe:
    if i in "0123456789":
        num += i
    elif i in "*+-/":
        oper += f"{i} "
        num += " "
    else:
        print("incorrect")
        quit()
for i in num.split():
    nums += [int(i)]
oper = oper.split()
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv
    }
if oper[0] == "*" or oper[0] == "/":
    print(ops[oper[1]](ops[oper[0]](nums[0], nums[1]), nums[2]))
else:
    print(ops[oper[0]](ops[oper[1]](nums[1], nums[2]), nums[0]))
