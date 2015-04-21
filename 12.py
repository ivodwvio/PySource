
def show(min, max, ending = True):
	for b in range(1, 10):
		for a in range(min, max + 1):
			print('{} * {} = {}'.format(a, b, a * b), end = '\t')
		print()
	if ending: print()

def main():
	'''Multiplication table'''
	show(1, 4)
	show(5, 8)
	show(9, 10, False)

if __name__ == '__main__': main()
