import turtle
import random

t0 = turtle.Turtle()
t0.speed(0)


def main():
    miVentana = turtle.Screen()
    miVentana.setup(width=800, height=800)
    miVentana.bgcolor("olive")
    posini = t0.pos()
    radio = 300
    inc = 0
    m = 0
    ang = 0
    colores = ["black", "gold", "black", "aquamarine",
               "gold", "turquoise", "black", "navy", "gold", "chocolate", "black", "darkgreen"]
    for j in range(60):
        for i in range(18):
            t0.begin_fill()
            t0.right(90)
            t0.forward(radio)
            t0.left(90)
            t0.color(colores[m], colores[m])
            t0.circle(radio, 10)
            t0.end_fill()
            t0.color(colores[m], colores[m])
            t0.begin_fill()
            t0.circle(radio, 10)
            t0.goto(posini[0], posini[1])
            t0.end_fill()
            m += 1
            if m == len(colores):
                m = 0
        radio -= 5
        t0.right(ang)
        ang += 0.05
    t0.ht()

    miVentana.exitonclick()


main()
