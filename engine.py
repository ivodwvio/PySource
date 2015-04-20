import inspect
import os

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
				module = __import__(command)
				func = getattr(module, 'main')
				func()
			except:
				print('Not implemented.')

def help():
	print('Command list:')
	print('help - display this menu')
	print('exit - stop the program')

	# get all files in the current directory
	files = [f for f in os.listdir('.') if os.path.isfile(f)]

	# get all modules that have a number for a name
	modules = []
	for f in files:
		name = os.path.splitext(f)[0]
		if name.isdigit():
			modules.append(f)

	# now get the doc for the main method of each file
	for m in modules:
		name = os.path.splitext(m)[0]
		module = __import__(name)
		solution = getattr(module, 'main')
		print(name, '-', inspect.getdoc(solution))

if __name__ == '__main__': main()
