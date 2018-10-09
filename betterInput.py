# Name: 			Andrew Udodov
# Student Number:  	10472552
# Date:				21/08/2018

from distutils.util import strtobool
import sys

if sys.version[0]=="2": input=raw_input

def choiceQuestionYesNo (question, errorMessage = 'Invalid input. \nPlease respond with \'yes\', \'y\', \'no\', or \'n\'.\n'):
	print ('%s [y/n] \n' %question)
	while True:
		try:
			return strtobool(input().lower())
		except ValueError: 
			print(errorMessage)
			continue

def inputInteger (prompt, errorMessage = 'Invalid input - Try again. \nRemember to use numbers only.',
             minValue = None, maxValue = None):
    while True:
        value = input(prompt)

        try:
            numResponse = int(value)
           
        except ValueError:
            print(errorMessage)
            continue

        if minValue is not None and numResponse < minValue:
            print('Please enter numbers between', minValue, 'and ',maxValue, '.')
            continue
            
        if maxValue is not None and numResponse > maxValue:
            print('Please enter numbers between', minValue, 'and ',maxValue, '.')
            continue
        
        return numResponse
