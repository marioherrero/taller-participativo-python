import turtle
t0 = turtle.Turtle()
t0.speed(0)
t1 = turtle.Turtle()
t1.speed(0)
t1.pencolor("red")


def ubicar(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def main():
    miVentana = turtle.Screen()
    miVentana.bgcolor("olive")
    t0.ht()
    t0.penup()
    t1.pensize(4)
    colores = [("red", "orange"), ("red", "gold")]
    m = 0
    for j in range(4):
        ang0 = 0
        ang1 = 0
        ang2 = 0
        if m == len(colores):
            m = 0
        t1.color(colores[m][0], colores[m][1])
        t1.begin_fill()
        for i in range(576):
            t0.seth(j*30)
            t0.right(ang0)
            t0.forward(150)
            t0.left(-ang1)
            t0.forward(75)
            t0.right(ang2)
            t0.forward(75)
            if i == 0:
                ubicar(t1, t0.pos()[0], t0.pos()[1])
                posini = t1.pos()
            else:
                t1.goto(t0.pos()[0], t0.pos()[1])
            ubicar(t0, 0, 0)
            t0.penup()
            ang0 += 2.5
            ang1 += 1.875
            ang2 += 1.875
        t1.goto(posini[0], posini[1])
        t1.end_fill()
        m += 1
    t1.ht()
    miVentana.exitonclick()


main()
