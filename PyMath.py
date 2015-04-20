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
				solution = getattr(module, 'main')
				solution()
			except:
				print('Not implemented.')

def help():
	print('Command list:')
	print('help - display this menu')
	print('exit - stop the program')
	files = [f for f in os.listdir('.') if os.path.isfile(f)]
	modules = []
	for f in files:
		if f[:4] == 'task':
			modules.append(f)
	for m in modules:
		name = os.path.splitext(m)[0]
		module = __import__(name)
		solution = getattr(module, 'main')
		print(name, '-', inspect.getdoc(solution))

if __name__ == '__main__': main()
