
def main():
	'''Calculate Exame Score'''
	count = int(input('Number of tasks: '))
	question = input('right or wrong answers? ')
	right = 0
	if question == 'right':
		right = int(input('Right answers: '))
	elif question == 'wrong':
		wrong = int(input('Wrong answers: '))
		right = count - wrong
	scale = 6
	print('Score:', scale/count * right)

if __name__ == '__main__': main()
