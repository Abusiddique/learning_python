"""
Script to get student marks data and calculate
total and average of marks
"""
import logging

logging.basicConfig(filename='student_data_logs.log', level=logging.DEBUG)

class StudentData():
	"""
	Functions:
		total - calculates total of marks
		average - calculates average of marks
	"""
	def __init__(self):
		logging.info('Getting marks as input from user')
		print("Enter the marks\n")
		self.english =  float(input("English="))
		self.tamil   =  float(input("Tamil="))
		self.maths   =  float(input("Maths="))
		self.science =  float(input("Science="))
		self.social  =  float(input("Social="))
		self.total   = 0

	def calculate_total(self):
		"""
		Calculates total of five subject marks
		"""
		logging.info('calculating total of the 5 subjects')
		self.total   = self.english + self.maths + self.tamil + self.science + self.social
		print("Total=" ,  self.total )
		
	def calculate_average(self):
		"""
		Calculates average of the marks
		"""
		logging.info('calculating average of the 5 subjects')
		avg = self.total / 5.0
		print("Average = " , avg )
		
obj1=StudentData()
option = int(input(" Enter the option \n 1. Total of a Student \n 2. Average of a Student \n"))

try:
	if option ==1:
		obj1.calculate_total()
	elif option == 2:
		obj1.calculate_total()
		obj1.calculate_average()
	else:
		print('Please enter a valid option (1/2). Exiting code')
except Exception as error:
	logging.exception('Exception: ' + str(error))
	print(error)
finally:
	logging.info('Done with processing')
