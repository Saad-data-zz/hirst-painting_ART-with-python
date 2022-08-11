#this code basically use colorfgram to extract the color from jpg file

# import colorgram
#
# rgb_color = []
# colors = colorgram.extract("Image.jpg", 30)
# #print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)

#print(rgb_color)
import turtle as turtle_module
import random

turtle_module.colormode(255)
t_baby = turtle_module.Turtle()

#increse the speed build-in function
t_baby.speed("fastest")

#this will not show the line of turtle
t_baby.penup()
t_baby.hideturtle()
color_list = [(220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (203, 134, 157),
              (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61),
              (197, 85, 112), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182),
              (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197),
              (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]

# set tim's position to the edge of the frame, to include all dots in the same frame

#the seatheading function will helps you to set the position of the begning of dots
#you have to set the value between 180 to 270, the half way of both value is 255
t_baby.setheading(225)

#setting our turtle on the starting poition
t_baby.forward(300)

#starting the position for coloum
t_baby.setheading(0)


number_of_dots = 100
#why we add the +1 in teh range because we have to print all the dots
for dot_count in range(1, number_of_dots + 1):
    t_baby.dot(20, random.choice(color_list))
    t_baby.forward(50)
#this line means that dividable on 10 only
    if dot_count % 10 == 0:
        t_baby.setheading(90)  # turn left by 90 degree
        t_baby.forward(40)
        t_baby.setheading(180)  # turn left again
        t_baby.forward(500)  # move forward 10 dots X 50 paces
        t_baby.setheading(0)  # face right

#display the screen
screen = turtle_module.Screen()
screen.exitonclick()