
def main():
	'''Odd numbers from 0 to 100'''
	count = 0
	for i in range(1, 101):
		if i % 2 != 0:
			print(i, end=' ')
			count += 1
			if (count % 10 == 0):
				print()

if __name__ == '__main__': main()
