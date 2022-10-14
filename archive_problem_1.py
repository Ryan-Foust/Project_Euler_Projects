#!/usr/bin/python3

# Problem:
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
debug = False

def is_multiple_of_5(num):
	return num % 5 == 0

def is_multiple_of_3(num):
	return num % 3 == 0

def main():
	if debug:
		print("Started main function")
	sum = 0	# store the answer
	for x in range(1000):	# look through each number up to maximum
		if debug:
			print("Testing number: "+str(x))
		if is_multiple_of_3(x) or is_multiple_of_5(x):
			if debug:
				print("Added "+str(x)+" to sum")
			sum += x
		else:
			if debug:
				print("Number "+str(x)+" was ignored")
			continue
	print("Sum was found to be "+str(sum))

if __name__ == "__main__":
	main()
