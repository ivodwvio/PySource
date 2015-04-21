# Python 3.4.3 Tutorial

the_world_is_flat = True
if the_world_is_flat:
	print('Be careful not to fall off!')

# this is the first comment
spam = 1 # and this is the second comment
		 # ... and now a third!
text = '# This is not a comment because it\'s inside quotes.'

print('2 + 2 =', 2 + 2)
print('50 - 5*6 =', 50 - 5*6)
print('(50 - 5*6) / 4 =', (50 - 5*6) / 4)
print('8 / 5 =', 8 / 5) # division always returns a floating point number
print('17 / 3', 17 / 3) # classic division returns a float
print('17 // 3 =', 17 // 3) # floor division discards the fractional part
print('17 % 3 =', 17 % 3) # the % operator returns the remainder of the division
print('5 * 3 + 2 =', 5 * 3 + 2) # result * divisor + remainder
print('5 ** 2 =', 5 ** 2) # 5 squared
print('2 ** 7 =', 2 ** 7) # 2 to the power of 7

width = 20
height = 5 * 9
result = width * height
print('result is', result)

print('3 * 3.75 / 1.5 =', 3 * 3.75 / 1.5)
print('7.0 / 2 =', 7.0 / 2)

tax = 12.5 / 100
price = 100.50
result = price * tax
result += price
print('result =', result)
print('round(result, 2) = ', round(result, 2))

print('spam eggs') # single quotes
print('doesn\'t') # use \' to escape the single quote...
print("doesn't") # or use double quotes instead
print('"Yes," he said.')
print("\"Yes,\" he said.")
print('"Isn\'t," she said.')

s = 'First line.\nSecond line.' # \n means newline
print(s)

print('C:\some\name') # here \n means newline!
print(r'C:\some\name') # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                    Display this usage message
     -H hostname           Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')
print('Py' 'thon')
prefix = 'Py'
print(prefix + 'thon')

text = ('Put several strings within parentheses '
		'to have them joined together.')
print(text)

word = 'Python'
print(word)
print(word[0]) # character in position 0
print(word[5]) # character in position 5
print(word[-1]) # last character
print(word[-2]) # second-last character
print(word[-6])

print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
print(word[2:5]) # characters from position 2 (included) to 5 (excluded)
print(word[:2] + word[2:])
print(word[:4] + word[4:])
print(word[:2]) # character from the beginning to position 2 (excluded)
print(word[4:]) # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end

#  P  y  t  h  o  n
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

print(word[4:42])
print(word[42:])
print('J' + word[1:])
print(word[:2] + 'py')

s = 'supercalifragilisticexpialidocious'
print(len(s))

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0]) # indexing returns the item
print(squares[-1])
print(squares[-3:]) # slicing returns a new list
print(squares[:]) # shallow copy of the list
print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125] # something's wrong here
print(4 ** 3) # the cube of 4 is 64, not 65!
cubes[3] = 64 # replace thw wrong value
print(cubes)

cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # and the cube of 7
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

letters = ['a', 'b', 'c', 'd']
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 10:
	print(b)
	a, b = b, a + b

i = 256 * 256
print('The value of i is', i)

a, b = 0, 1
while b < 1000:
	print(b, end=',')
	a, b = b, a + b
print()

x = 2 # int(input('Please enter an integer: '))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))

for w in words[:]: # loop over a slice copy of the entire list.
	if len(w) > 6:
		words.insert(0, w)
print(words)

for i in range(5):
	print(i, end=' ')
print()

for i in range(5, 10):
	print(i, end=' ')
print()

for i in range(0, 10, 3):
	print(i, end=' ')
print()

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])

print(list(range(5)))

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n // x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')

for num in range(2, 10):
	if num % 2 == 0:
		print('Found an even number', num)
		continue
	print('Found a number', num)

# while True:
#	pass # Busy-wait for keyboard interrupt (Ctrl+C)

class MyEmptyClass:
	pass

def initlog(*args):
	pass # Remember to implement this!

def fib(n): # write Fibonacci series up to n
	'''Print a Fibonacci series up to n.'''
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()

# Now call the function we just defined:
fib(2000)
f = fib
f(100)

def fib2(n): # return Fibonacci series up to n
	'''Return a list containing the Fibonacci series up to n.'''
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result

f100 = fib2(100)
print(f100)

def ask_ok(prompt, retries = 4, complaint = 'Yes or no, please!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		elif ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries -= 1
		if retries < 0:
			raise OSError('uncooperative user')
		print(complaint)

i = 5

def f(arg = i):
	print(arg)

i = 6
f()

def f(a, L = []):
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))

def f(a, L = None):
	if L is None:
		L = []
	L.append(a)
	return L

print(f(1))
print(f(2))
print(f(3))

def parrot(voltage, state = 'a stiff', action = 'voom', type = 'Norwegian Blue'):
	print('-- This parrot wouldn\'t', action, end=' ')
	print('if you put', voltage, 'volts through it.')
	print('-- Lovely plumage, the', type)
	print('-- It\'s', state, '!')

parrot(1000)
parrot(voltage = 1000)
parrot(voltage = 1000000, action = 'VOOOOOM')
parrot(action = 'VOOOOOM', voltage = 1000000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state = 'pushing up the daisies')

def cheeseshop(kind, *arguments, **keywords):
	print('-- Do you have any', kind, '?')
	print('-- I\'m sorry, we\'re all out of', kind)
	for arg in arguments:
		print(arg)
	print('-' * 40)
	keys = sorted(keywords.keys())
	for kw in keys:
		print(kw, ':', keywords[kw])

cheeseshop('Limburger', 'It\'s very runny, sir.',
		   'It\'s really very, VERY runny, sir.',
		   shopkeeper = 'Michael Palin',
		   client = 'John Cleese',
		   sketch = 'Cheese Shop Sketch')

def write_multiple_items(file, separator, *args):
	file.write(separator.join(args))

def concat(*args, sep = '/'):
	return sep.join(args)

print(concat('earth', 'mars', 'venus'))
print(concat('earth', 'mars', 'venus', sep = '.'))

print(list(range(3, 6)))
args = [3, 6]
print(args)
print(list(range(*args)))

def parrot(voltage, state = 'a stiff', action = 'voom'):
	print('-- This parrot wouldn\'t', action, end = ' ')
	print('if you put', voltage, 'volts through it.', end=' ')
	print('E\'s', state, '!')

d = {'voltage': 'four million', 'state': 'bleedin\' demised', 'action': 'voom'}
parrot(**d)

def make_incrementor(n):
	return lambda x: x + n

f = make_incrementor(42)

f(0)
f(1)
