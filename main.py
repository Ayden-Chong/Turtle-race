import turtle
import random

track_x, track_y, track_len, track_width, lane_width = (-350, 200, 700, 400, 100)
lane_x, lane_y, finish_x, turtle_x, turtle_y = (-380, 130, 250, -300, 150)


def draw_track():
    turt.goto(track_x, track_y)
    turt.color("chocolate")
    turt.pendown()
    turt.begin_fill()
    for i in range(2):
        turt.forward(track_len)
        turt.right(90)
        turt.forward(track_width)
        turt.right(90)

    turt.end_fill()
    turt.color("white")
    for a in range(5):
        turt.penup()
        turt.goto(track_x, track_y - lane_width * a)
        turt.pendown()
        turt.forward(track_len)
    turt.penup()
    for a in range(4):
        turt.goto(lane_x, lane_y - lane_width * a)
        turt.write(a + 1, font=("Arial", 20, "bold"))


def draw_finishline():
    turt.penup()
    turt.goto(finish_x, track_y)
    turt.seth(270)
    turt.pendown()
    turt.begin_fill()
    for i in range(2):
        turt.forward(track_width)
        turt.left(90)
        turt.forward(40)
        turt.left(90)
    turt.end_fill()

    turt.penup()
    turt.color("black")
    turt.goto(turt.xcor() + 20, turt.ycor())
    turt.pendown()
    turt.begin_fill()
    for i in range(10):
        turt.forward(20)
        turt.left(90)
        turt.forward(20)
        turt.left(90)
        turt.forward(20)
        turt.left(90)
        turt.forward(20)
        turt.left(90)
        turt.forward(40)
        turt.right(90)
        turt.forward(20)
        turt.right(90)
        turt.forward(20)
        turt.right(90)
        turt.forward(20)
        turt.right(90)
        turt.forward(20)
    turt.end_fill()


def setup_screen():
    global turt, screen

    screen = turtle.getscreen()
    screen.setup(800, 500)
    screen.title("Racing turtle game")
    screen.bgcolor("#9F4123")
    turt = turtle.getturtle()
    turt.speed(7)
    turt.penup()
    turt.goto(-100, 205)
    turt.color("white")
    turt.write("Racing Turtles", font=("Arial", 20, "bold"))
    draw_track()


def setup_turtles():
    global turtle1, turtle2, turtle3, turtle4
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle3 = turtle.Turtle()
    turtle4 = turtle.Turtle()
    global turtlelist
    turtlelist = [turtle1, turtle2, turtle3, turtle4]
    colorlist = ["blue", "pink", "red", "green"]
    for i in range(4):
        currentturt = turtlelist[i]
        currentturt.penup()
        currentturt.color(colorlist[i])
        currentturt.shape("turtle")
        currentturt.turtlesize(2)
        currentturt.goto(turtle_x, turtle_y - lane_width * i)
        currentturt.pendown()


def get_userguess():
    return screen.numinput("Guess!", "Which turtle will win?(1, 2, 3 or 4", minval=1, maxval=4)


def race(user_guess: int):
    while (
            turtle1.xcor() <= finish_x and turtle2.xcor() <= finish_x and turtle3.xcor() <= finish_x and turtle4.xcor() <= finish_x):
        turtle1.forward(random.randint(1, 15))
        turtle2.forward(random.randint(1, 15))
        turtle3.forward(random.randint(1, 15))
        turtle4.forward(random.randint(1, 15))
    for i in range(4):
        if turtlelist[i].xcor() > finish_x:
            winner = i + 1
            turtlelist[i].shapesize(2.5)
            print(winner)
    for i in range(99999999999):
        turtlelist[winner - 1].right(5)

    if (user_guess == winner):
        screen.textinput("Game over!",
                         "You win! Turtle" + str(winner) + "won the game")
    else:
        screen.textinput("Game over!",
                         "You lose! Turtle" + str(winner) + "won the game")


def main():
    setup_screen()
    draw_finishline()
    setup_turtles()
    user_guess = get_userguess()
    race(user_guess)


if __name__ == "__main__":
    main()
