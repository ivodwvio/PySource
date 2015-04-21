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
		elif command == 'next':
			files = [f for f in os.listdir('.') if os.path.isfile(f)]
			count = 0
			for f in files:
				name = os.path.splitext(f)[0]
				if name.isdigit():
					count += 1
			print('Next is', count + 1)
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

	files = [f for f in os.listdir('.') if os.path.isfile(f)]

	modules = []
	for f in files:
		name = os.path.splitext(f)[0]
		if name.isdigit():
			modules.append(name)

	modules.sort(key = int)
	for m in modules:
		module = __import__(m)
		solution = getattr(module, 'main')
		print(m, '-', inspect.getdoc(solution))

if __name__ == '__main__': main()
