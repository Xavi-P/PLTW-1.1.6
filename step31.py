import turtle as trtl

painter = trtl.Turtle()
painter.pensize(40)

# Create a spider body
painter.circle(20)

# Configure spider legs

num_branches =8
branch_length =50
branch_angle = 360 / num_branches
print("z=", branch_angle)
painter.pensize(5)
branch_num= 0

# Draw legs

while (branch_num < num_branches):
  
  
  while branch_num < num_branches:
    painter.goto(0,20)
    if branch_num== 4:
        painter.setheading(branch_angle*branch_num + 30
        )
    else:
        painter.setheading(branch_angle*branch_num+25
        )
    branch_num+= 1
    painter.forward(branch_length)
    print("z*n=", branch_angle*branch_num)
# create eyes
painter.goto(-30,10)
painter.color("white")
painter.circle(1)
painter.penup()
painter.goto(-30,20)
painter.pendown()
painter.circle(1)
painter.color("black")
 
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
