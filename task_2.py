import turtle

window = turtle.Screen()
window.bgcolor("white")
window.title("Фрактальне Дерево")

t = turtle.Turtle()
t.speed(0) 
t.hideturtle()
t.pensize(1)

def draw_branch(branch_length, depth):
    if depth < 1:
        return

    t.forward(branch_length)
    t.left(30)
    draw_branch(branch_length * 0.7, depth - 1)
    t.right(60)
    draw_branch(branch_length * 0.7, depth - 1)
    t.left(30)
    t.backward(branch_length)

t.penup()
t.goto(0, -200)
t.pendown()
t.left(90)


depth = window.numinput(
    'Налаштування',
    'Введіть глибиину рекурсії (1-12): ',
    default=7,
    minval=1,
    maxval=15
)

draw_branch(100, depth)
turtle.done()