# PyMath.py

import inspect
import PyMath

def main():
	running = True
	while running:
		command = input('>')
		if command == 'exit':
			running = False
		elif command == 'help':
			help()
		else:
			try:
				globals()[command]()
			except:
				print('Not implemented.')

def help():
	print('Command list:')
	print('help - display this menu')
	print('exit - stop the program')
	for name, obj in inspect.getmembers(PyMath):
		if inspect.isfunction(obj) and name[:4] == 'task':
			print(name, '-', inspect.getdoc(obj))

# Show the numbers from 0 to 9
def task1():
	''' Show the numbers from 0 to 9 '''
	for i in range(10):
		print(i, end=' ')
	print()

# Show the numbers from 0 to 100
def task2():
	''' Show the numbers from 0 to 100 '''
	for i in range(101):
		if (i % 10 == 0 and i != 0):
			print()
		print(i, end=' ')
	print()

if __name__ == '__main__': main()
