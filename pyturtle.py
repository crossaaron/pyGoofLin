#! /usr/bin/env python

import turtle
	
def triangle():
	for side in range(3):
		turtle.forward(100)
		turtle.right(120)
		
def rec_turtle(r):
	if r >= 10:
		turtle.pendown()
		turtle.circle(r)
		turtle.penup()
		for j in range (4):
			turtle.left(90)
			turtle.forward(r)
			turtle.left(90)
			turtle.forward(r)
			turtle.left(90)
			rec_turtle(r/2)
	

if __name__=="__main__":
	import random
	colours=["red","orange","yellow","green","blue"]
	turtle.speed="fastest"
	for j in range(72):
		turtle.color(random.choice(colours))
		rec_turtle(100)
		turtle.left(5)	
		turtle.exitonclick()	
		
