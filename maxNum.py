'''
numbers = []
inp = 1
while inp != 0:
	inp = int(input("Please enter a number: "))
	numbers.append(inp)
	#print(numbers)
	maxim = max(numbers)
	if inp ==0:
		print("this is the max:", maxim)
		break;
'''		
		
for row in range(1,6):
	for col in range(1,6):
		print(row*col, end=" - ")
	print()