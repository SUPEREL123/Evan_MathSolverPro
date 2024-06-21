import math
import turtle
import time
from PIL import Image




def drawing_triangle(angle1, angle2, h, save_path= None):
    angle3 = 90
    if angle1 + angle2 != 90:
        raise Exception("Angle 1 + angle 2 must be equal 90")

    #           |\ <-- angle 2
    #           | \
    #  (side2)  |  \ (h)
    #           |   \
    # angle3--> |____\ <-- angle 1
    #           (side3)


    side2 = math.sin(math.radians(angle1))*h
    side3 = math.cos(math.radians(angle1))*h
    
    # turn the turtle to face up
    turtle.left(90)
    # moving up
    turtle.forward(side2)
    # turn the turtle to face angle 1
    turtle.right(180-angle2)
    # move the turtle to the longest side of the triangle
    turtle.forward(h)
    # turn the turtle to face angle 3
    turtle.right(180-angle1)
    # move the turtle toward angle 3
    turtle.forward(side3)
    
    time.sleep(5)

    # # Save the image
    # ts = turtle.getscreen()
    # ts.getcanvas().postscript(file="temp.eps")
    # img = Image.open("temp.eps")
    # img.save(save_path, "PNG")

    # turtle.done()



# angle1 = 2
# angle2 = 90
# angle3 = 180-angle1-angle2
# h = 100
# side2 = math.sin(math.radians(angle1))*h
# side3 = math.cos(math.radians(angle1))*h



# turtle.left(90)
# turtle.forward(side2)
# turtle.right(angle2)
# turtle.forward(side3)
# turtle.right(90+angle3)
# turtle.forward(h)





# time.sleep(10)


# equation of straight line
def plus(input_string):
  input_value = input_string.split("+")
  current_sum = 0
  for value in input_value:
    current_sum = current_sum + float(value)
  return current_sum


def multiply(input_string):
  input_value = input_string.split("*")
  current_product = 1
  for value in input_value:
    current_product = current_product * float(value)
  return current_product


def equation_of_st_line(x1, y1, x2, y2, draw = False):
  slope = ((y2 - y1)/(x2 - x1))
  y_intercept = slope * -x1 + y1


  slope = round(slope, 3)
  y_intercept = round(y_intercept, 3)


  answer = f"y = {slope}x + {y_intercept}"

  if draw == True:
    drawing_st_line(slope, y_intercept)

  return answer


def distance_between_two_pt(x1, y1, x2, y2):
  answer = ((x2-x1)**2 + (y2-y1)**2)**0.5
  answer = round(answer, 3)
  return answer


def drawing_st_line(slope, y_intercept):
    turtle.goto(0,100)
    turtle.goto(0,-100)
    turtle.goto(0,0)
    turtle.goto(-100,0)
    turtle.goto(100,0)
    turtle.up()
    turtle.goto(0,0)
    for x in range(-20, 21):
        y = slope * x + y_intercept
        turtle.goto(x,y)
        turtle.down()



    time.sleep(5)




# answer = equation_of_st_line(-3,8,-19,-53, draw = True)
# print(answer)

# drawing_triangle(23,90,100, "triangle.png")