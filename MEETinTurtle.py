
import turtle

# Everything that comes after the # is a 
# comment.
# It is a note to the person reading the code.
# The computer ignores it.
# Write your code below here...


# ...and end it before the next line.



turtle.penup() 	#Brings the pen up, so
				#nothing will be drawn
	#Puts the pen down, so we
				#are ready to draw!
turtle.goto(10,20) #Go to the position “x"&"y", 
#but write in numbers 
#instead 

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
turtle.goto(-50, -100)
turtle.goto(+50,-100)
turtle.goto(-50,-100)
turtle.goto(-50,+100)
turtle.goto(+50,+100)
turtle.goto(-50,+100)
turtle.goto(-50,+0)
turtle.goto(+50,0)
turtle.penup()
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(100,100)
turtle.goto(200,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(200,0)
turtle.goto(100,0)
turtle.goto(100,-100)
turtle.pendown()
turtle.goto(200,-100)
turtle.goto(300,-100)
turtle.goto(300,200)
turtle.goto(300,100)
turtle.goto(300,-100)



turtle.mainloop()

