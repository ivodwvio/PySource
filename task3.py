
def main():
	''' Show the numbers from 0 to 100 '''
	for i in range(101):
		if (i % 10 == 0 and i != 0):
			print()
		print(i, end=' ')
	print()

if __name__ == '__main__': main()
