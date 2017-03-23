# an example Python script to draw a geometric shapes in specific patterns

import random
import turtle


# an example of how to use these methods
def go_turtle_go():

    nice_turtle = turtle.Turtle()
    draw_grid_of_randomly_colored_squares(nice_turtle, 5, 25, 5)


# the specified turtle will draw a polygon with the given number of sides,
# wsith each side as long as the specified length
def draw_polygon(the_turtle, side_count, side_length, color=(0, 0, 0)):

    angle = 360 / side_count
    the_turtle.pendown()
    the_turtle.fillcolor(color)
    the_turtle.fill(True)
    for i in range(side_count):
        the_turtle.forward(side_length)
        the_turtle.right(angle)
    the_turtle.fill(False)


# the specified turtle will draw a square of the given size, randomly colored
# centered around itself
def draw_randomly_colored_square(the_turtle, side_length):

    offset = side_length / 2
    x, y = the_turtle.position()
    the_turtle.penup()
    the_turtle.goto(x-offset, y-offset)
    random_color = (random.random(), random.random(), random.random())
    draw_polygon(the_turtle, 4, side_length, random_color)
    the_turtle.penup()
    the_turtle.goto(x, y)


# the specified turtle will draw a row of squares
def draw_row_of_squares(the_turtle, square_count, square_size, square_spacing):

    x, y = the_turtle.position()
    jump = square_size + square_spacing
    for i in range(square_count):
        the_turtle.pendown()
        draw_randomly_colored_square(the_turtle, square_size)
        the_turtle.penup()
        the_turtle.forward(jump)
    the_turtle.goto(x, y)


# the specified turtle will draw a grid of squares centered around its current position
def draw_grid_of_randomly_colored_squares(the_turtle, grid_size, square_size, square_spacing):

    x, y = the_turtle.position()
    jump = square_size + square_spacing
    for i in range(grid_size):
        the_turtle.goto(x, y + i*jump)
        draw_row_of_squares(the_turtle, grid_size, square_size, square_spacing)
    the_turtle.goto(x, y)
