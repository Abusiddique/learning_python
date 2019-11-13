"""
Script to perform few operations like
Addition, subtraction, multiplication, division
"""
import sys
from functools import reduce

def get_input():
	"""Get inputs from the user"""
	
	list_of_numbers = input("Enter the numbers")
	list_of_numbers = list_of_numbers.split(',')
	list_of_numbers = [float(number) for number in list_of_numbers]
	if len(list_of_numbers) < 2:
		print('Please enter atleast 2 numbers to proceed with calculations')
		sys.exit(1)
	return list_of_numbers
		
def add(list_of_numbers):
	sum_of_numbers = sum(list_of_numbers)
	print("Sum of numbers", sum_of_numbers)

def sub(list_of_numbers):
	subtraction_of_numbers = list_of_numbers[0] - sum(list_of_numbers[1:])
	print("Subraction of two number", subtraction_of_numbers)

def mul(list_of_numbers):
	product_of_numbers = reduce((lambda x, y: x * y),  list_of_numbers)
	print("Multiplication of two numbers", product_of_numbers)

def div(list_of_numbers):
	division_of_numbers = reduce((lambda x, y: x /y),  list_of_numbers)
	print("Division of two numbers", division_of_numbers)

def validate_option(list_of_numbers):
	
	option = int(input("Enter the option to calculate \n1.Add \n2.Subtrate \n3.Multiplication\n4.Division\n5.Exit\n "))
	if option ==1:
		add(list_of_numbers)
	elif option ==2:
		sub(list_of_numbers)
	elif option ==3:
		mul(list_of_numbers)
	elif option ==4:
		div(list_of_numbers)
	else:
		sys.exit(0)
	continue_option=input("Do you want to Continue y/n\n")
	if continue_option=='y':
		validate_option(list_of_numbers)
	else:
		sys.exit(0)
list_of_numbers = get_input()
validate_option(list_of_numbers)

