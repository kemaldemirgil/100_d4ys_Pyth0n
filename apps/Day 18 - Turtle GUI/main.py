import turtle
from turtle import Turtle, Screen
import random
import colorgram as cg
turtle.colormode(255)
# color_list = cg.extract("IMG_1914.JPG", 24)
# image_colors = []
# for extracted_color in color_list:
#     print(list[extracted_color.rgb])
#     image_colors.append(tuple(extracted_color.rgb))
#
color_pallette = [(34, 12, 10), (213, 65, 12), (254, 137, 33), (138, 30, 19), (250, 89, 16), (254, 213, 62), (34, 9, 11), (123, 24, 27), (4, 6, 3), (166, 44, 48), (230, 123, 12), (254, 252, 132), (9, 8, 12), (205, 65, 66)]
print(color_pallette)
print(len(color_pallette))


# directions = ["right", "forward", "left"]
# colors = ["blue", "pink", "red", "purple"]
kenny = Turtle()
kenny.shape("classic")
kenny.speed("fastest")
kenny.hideturtle()

kenny.penup()

kenny.setheading(225)
kenny.forward(300)
kenny.setheading(0)


def dot_line():
    for _ in range(9):
        kenny.dot(40, random.choice(color_pallette))
        kenny.forward(50)
        kenny.dot(40, random.choice(color_pallette))


def draw_cycle():
    dot_line()
    kenny.left(90)
    kenny.forward(50)
    kenny.left(90)
    dot_line()
    kenny.right(90)
    kenny.forward(50)
    kenny.right(90)


for _ in range(5):
    draw_cycle()


# kenny.pensize(2)
# i = 0
# while i < 360:
#     kenny.pencolor((random.choice(range(255)), random.choice(range(255)), random.choice(range(255))))
#     kenny.setheading(i)
#     kenny.circle(100)
#     i += 5

screen = Screen()
# screen.setup(600, 600)

screen.exitonclick()
#
# i = 3
# while i < 10:
#     kenny.color(random.choice(colors))
#     for _ in range(i):
#         current_angle = 360 / i
#         kenny.forward(100)
#         kenny.right(current_angle)
#     i += 1

# walk_amount = 0
# while walk_amount < 300:
#     random_direction = random.choice(directions)
#     kenny.pencolor((random.choice(range(255)), random.choice(range(255)), random.choice(range(255))))
#     if random_direction == "right":
#         kenny.right(90)
#         kenny.forward(10)
#     if random_direction == "left":
#         kenny.left(90)
#         kenny.forward(10)
#     if random_direction == "forward":
#         kenny.forward(10)
#     walk_amount += 1


# for _ in range(4):
#     for _ in range(10):
#         kenny.forward(10)
#         kenny.penup()
#         kenny.forward(10)
#         kenny.pendown()
#     kenny.left(90)
