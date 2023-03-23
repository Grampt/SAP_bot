import turtle
import sqlite3

coord_dict = {"A1": [0, 0], "A2": [0, 0], "A3": [0, 0], "A4": [0, 0], "A5": [0, 0],
              "B1": [0, 0], "B2": [0, 0], "B3": [0, 0], "B4": [0, 0], "B5": [0, 0],
              "C1": [0, 0], "C2": [0, 0], "C3": [0, 0], "C4": [0, 0], "C5": [0, 0],
              "D1": [0, 0], "D2": [0, 0], "D3": [0, 0], "D4": [0, 0], "D5": [0, 0],
              "E1": [0, 0], "E2": [0, 0], "E3": [0, 0], "E4": [0, 0], "E5": [0, 0]}
img_width = 500
img_height = 500

image_dims = [img_height, img_width]

turtle1 = turtle


def get_image():
    return


def coord_shift(height, width, dictionary):
    loop_limit = 0

    width_step = width / 5
    height_step = height / 5
    width_curr = width_step / 2
    height_curr = height_step / 2

    width_change = width_curr
    height_change = height_curr

    new_dict = dictionary

    for x in new_dict:
        if loop_limit == 0:
            new_dict.update({x: [height_change, width_change]})
            loop_limit += 1
        else:
            width_change += width_step
            new_dict.update({x: [height_change, width_change]})
            loop_limit += 1
            if loop_limit == 5:
                loop_limit = 0
                width_change = width_curr
                height_change = height_change + height_step
        print(x, " ", new_dict[x])
    return new_dict


def draw_arrows(image_size, start, end, coord_list):
    coord_group = coord_shift(image_size[0], image_size[1], coord_list)
    turtle1.width(5)
    turtle1.screensize(image_size[1], image_size[0], bg=None)

    if start == end:
        turtle1.setpos(coord_group[start])
        turtle1.circle(10)
    else:
        return


# turtle1.color('red', 'yellow')
# turtle1.begin_fill()
# turtle1.hideturtle()
# turtle1.width(6)
# while True:
#     turtle1.forward(200)
#     turtle1.left(130)
#     if abs(turtle1.pos()) < 1:
#         break
# turtle1.end_fill()
# turtle1.done()

coord_shift(img_height, img_width, coord_dict)
