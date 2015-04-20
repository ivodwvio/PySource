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
			modules.append(f)
	for m in modules:
		name = os.path.splitext(m)[0]
		module = __import__(name)
		solution = getattr(module, 'main')
		print(name, '-', inspect.getdoc(solution))

if __name__ == '__main__': main()
