'''

	Moshe Berman
	Professor Zhou
	CISC 3150
	Spring 2014

	Assignment 2

'''

#	This function computes the volume of a sphere, given its radius
def radiusOfSphere(radius):
	return math.pi * pow(radius,3)

#	This function calculates the real roots of a quadratic equation
def realRootsUsingCoefficients(a, b, c):
	
	discRoot = math.sqrt(b * b - 4 * a * c)
	root1 = (-b + discRoot) / (2 * a)
	root2 = (-b - discRoot) / (2 * a)

#	Return the number of zeros in a list of numbers
def zeroesInList(numbers):
	return sum(x == 0 for row in numbers)

#	Return largest and smallest in list
def maxAndMinInList(numbers):
	return list(min(numbers), max(numbers))

#	Print n rows in pascals triangle
def pascalsTriangle(n):

	for i in xrange(1, n):

		output = ""
		for x in xrange(1,i):
			output += str(x) + " "

		print output