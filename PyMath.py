
for i in range(10):
	print(i, end=' ')
print()

running = True
while running:
	command = input()
	if command == 'exit':
		running = False
