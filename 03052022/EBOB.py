# x, y = map(int, input("Type two numbers separated by space: ").split(" "))
# if x > y:
# 	s = y
# else:
# 	s = x
# while True:
# 	if x % s == 0 and y % s == 0:
# 		print(s)
# 		break
# 	else:
# 		s-=1

# x = int(input("Type a numnberL "))
# s = 0
# for i in range(2, x + 1):
# 	c = 0
# 	for j in range(2, i):
# 		if i % j == 0:
# 			c = 1
# 			break
# 	if c == 1:
# 		continue
# 	if x % i == 0:
# 		if s != i:
# 			print(i, end=" ")
# 			s = i
# 		x //= i
# 		if x == 1:
# 			break

def whole(x):
	x = int(x)
	result = ""
	while x != 0:
		if x % 2 == 1:
			result += "1"
		else:
			result += "0"
		x //= 2
	return result[::-1]

def floated(x):
	x %= 1
	result = ""
	while True:
		x *= 2
		if x >= 1:
			result += "1"
		else:
			result += "0"
		if x == 1:
			break
	return result

while True:
	try:
		string = input("Enter decimal number: ")
		if "." in string:
			string = float(string)
			result_whole = whole(string)
			result_float = floated(string)
			print(f"{result_whole}.{result_float}")

		else:
			result = whole(string)
			print(result)
	except KeyboardInterrupt:
		print("You pushed interruption key.\n\nApplication closed")
		break