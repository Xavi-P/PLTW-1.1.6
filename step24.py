import turtle as trtl

painter = trtl.Turtle()
painter.pensize(40)

# Create a spider body
painter.circle(5)

# Configure spider legs

num_branches =5
branch_length =50
branch_angle_range = 360 / num_branches
print("z=", branch_angle_range)
painter.pensize(5)
branch_num= 0

# Draw legs

while (branch_num < num_branches):
  print("z*n=", branch_angle_range*branch_num)
  painter.goto(0,0)
  painter.setheading(branch_angle_range*branch_num)
  painter.forward(branch_length)
  # n=next step's angle
  branch_num = branch_num + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
