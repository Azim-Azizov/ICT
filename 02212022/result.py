while True:
	x, y = map(float, input("Enter coordinates (separate by space): ").split(" "))
# 	if x**2+y**2>1 or (x>0 and y<0) or (x>0 and y>0 and x>y) :
# 		print("is not inside figure")
# 	else:
# 		print("is inside figure")
	if x**2>=y and y>=0 and ((y<=2-x and x>0) or (y>=2-x and x<0)):
		print("inside figure")
	else:
		print("outside figure")