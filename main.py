import sys
import string
import os
import datetime
import time
import random
from random import *
from time import sleep

pwch = string.ascii_letters
pwnm = string.digits
pwnmch = string.ascii_letters + string.digits

def kill():
	sleep(0.3)
	sys.exit()

def mainMenu():
	sleep(0.3)
	confirm = input(" Press enter to continue, or e to exit\n ")
	sleep(0.3)
	os.system('clear')

	if confirm == "":
		sleep(0.3)
		os.system('clear')
		menu()

	elif confirm == "e":
		sleep(0.3)
		os.system('clear')
		kill()

	else:
		sleep(0.3)
		print(f' Invalid input "{confirm}"')
		sleep(1)
		os.system('clear')
		mainMenu()

def menu():
	sleep(0.3)
	ask = input(" Would you like to generate a password with numbers (n), characters (ch), or both? (nch)\n ")

	if ask == "n":
		sleep(0.3)
		os.system('clear')
		generatenumpass()

	elif ask == "ch":
		sleep(0.3)
		os.system('clear')
		generatecharpass()

	elif ask == "nch":
		sleep(0.3)
		os.system('clear')
		generatecharnum()

	else:
		sleep(0.3)
		print(f' Invalid input "{ask}"')
		sleep(1)
		os.system('clear')
		menu()

def generatenumpass():
	try:
		sleep(0.3)
		minrg = int(input(" Minimum range: "))
		sleep(0.3)
		maxrg = int(input(" Maximum range: "))
		sleep(0.3)

		print(" Generating...")

		passres = ''.join(choice(pwnm) for x in range(randint(minrg, maxrg)))

		sleep(2)
		# os.system('clear')
		print(f' Generated password with numbers: {passres}\n Generated at: {datetime.datetime.now().strftime("%I:%M:%S %p")}')

		sleep(0.3)

		askagain = input(' Generate again? (yes, no)\n ')

		if askagain == 'yes':
			generatecharnum()

		elif askagain == 'no':
			kill()

	except ValueError:
		sleep(0.3)
		print(' Please type a number, not a character!')
		generatenumpass()

def generatecharpass():
	try:
		sleep(0.3)
		minrg = int(input(" Minimum range: "))
		sleep(0.3)
		maxrg = int(input(" Maximum range: "))
		sleep(0.3)

		print(" Generating...")

		passres = ''.join(choice(pwch) for x in range(randint(minrg, maxrg)))

		sleep(2)
		# os.system('clear')
		print(f' Generated password with characters: {passres}\n Generated at: {datetime.datetime.now().strftime("%I:%M:%S %p")}')

		sleep(0.3)

		askagain = input(' Generate again? (yes, no)\n ')

		if askagain == 'yes':
			generatecharnum()

		elif askagain == 'no':
			kill()

	except ValueError:
		sleep(0.3)
		print(' Please type a number, not a character!')
		generatecharpass()

def generatecharnum():
	try:
		sleep(0.3)
		minrg = int(input(" Minimum range: "))
		sleep(0.3)
		maxrg = int(input(" Maximum range: "))
		sleep(0.3)

		print(" Generating...")

		passres = ''.join(choice(pwnmch) for x in range(randint(minrg, maxrg)))

		sleep(2)
		# os.system('clear')
		print(f' Generated password with characters and numbers: {passres}\n Generated at: {datetime.datetime.now().strftime("%I:%M:%S %p")}')

		sleep(0.3)

		askagain = input(' Generate again? (yes, no)\n ')

		if askagain == 'yes':
			generatecharnum()

		elif askagain == 'no':
			kill()

	except ValueError:
		sleep(0.3)
		print(' Please type a number, not a character!')
		generatecharnum()

mainMenu()
