import turtle

def main():
	'''Draw triangle with turtle'''
	window = turtle.Screen()
	window.bgcolor('green')
	tom = turtle.Turtle()
	tom.forward(100)
	tom.left(120)
	tom.forward(100)
	tom.left(120)
	tom.forward(100)
	window.exitonclick()

if __name__ == '__main__': main()
