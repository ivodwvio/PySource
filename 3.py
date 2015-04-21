
def main():
	'''Numbers from 0 to 100'''
	print(0, end=' ')
	for i in range(1, 101):
		if (i % 10 == 0):
			print()
		print(i, end=' ')
	print()

if __name__ == '__main__': main()
