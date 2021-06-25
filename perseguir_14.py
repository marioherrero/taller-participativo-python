################################################
###                                          ###
###   09/04/2020                             ###
###   Autor: Mario Antonio Herrero Machado   ###
###   perseguir_14.py                        ###
###   8 tortugas se persiguen - turtle.py    ###
###                                          ###
################################################
import turtle
import random
import math

t0 = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t8 = turtle.Turtle()
tortugas = [t0, t1, t2, t3, t4, t5, t6, t7, t8]
for i in range(9):
    tortugas[i].speed(0)
    tortugas[i].pensize(3)
colores = ["maroon", "darkorange", "firebrick", "green", "maroon", "darkorange", "gold", "firebrick",
           "chocolate", "orange", "orangered", "red", "maroon", "orange", "green", "maroon", "darkorange", "firebrick",
           "chocolate", "orange", "orangered", "red", "maroon", "orange"]

################################################
###  Definicion de Funciones                 ###
################################################


def hacia(t1, t2):
    lx = t2.xcor()-t1.xcor()
    ly = t2.ycor()-t1.ycor()
    lx2 = lx*lx
    ly2 = ly*ly
    h = math.sqrt(lx2+ly2)
    if h == 0:
        ang = 0
    else:
        ang = math.degrees(math.asin(lx/h))

    if lx < 0 and ly > 0:
        t1.seth(90)
        t1.right(ang)
    elif lx < 0 and ly < 0:
        t1.seth(270)
        t1.right(-ang)
    elif lx > 0 and ly > 0:
        t1.seth(90)
        t1.right(ang)
    elif lx > 0 and ly < 0:
        t1.seth(270)
        t1.right(-ang)
    elif t2.ycor() == t1.ycor() and t2.xcor() < t1.xcor():
        t1.seth(180)
    else:
        # t1.pencolor("green")
        t1.dot(20)
        # t1.forward(pasos1)


def ubicar_8t(tortugas, radio, ang1):
    ang = 0
    for i in range(8):
        tortugas[i].seth(0)
        tortugas[i].penup()
        tortugas[i].goto(0, 0)
        tortugas[i].right(ang+ang1)
        tortugas[i].forward(radio)
        tortugas[i].pendown()
        ang += 45


def ubicar_t(t, x, y):
    t.penup()
    t.goto(x, y)
    t.seth(0)
    # t.pendown()


def main():
    miVentana = turtle.Screen()
    miVentana.bgcolor("black")
    miVentana.title("Perseguir_14")
    radio = 100
    ubicar_8t(tortugas, 300, 0)
    ubicar_t(t8, 0, 0)
    ang1 = 0
    t8.pensize(1)
    for i in range(8):
        tortugas[i].pencolor(colores[i])
    radio = 25
    for j in range(5):
        ubicar_8t(tortugas, 300, ang1)
        radio2 = 10
        for k in range(80):
            # t8.right(6)
            # t8.forward(radio)
            for i in range(8):
                tortugas[i].pencolor(random.choice(colores))
                if i < 7:
                    hacia(tortugas[i], tortugas[i+1])

                    tortugas[i].forward(radio2)
                else:
                    hacia(tortugas[i], tortugas[0])
                    tortugas[i].forward(radio2)
            print("estoy en el primer loop", k)
            #radio += 2
            #radio2 += 0.025
        radio2 = 10
        ubicar_8t(tortugas, 300, ang1)
        for k in range(40):
            for i in range(7):
                tortugas[i].pencolor(random.choice(colores))
                if i < 6:
                    hacia(tortugas[i], tortugas[i+2])
                    tortugas[i].forward(radio2)
                else:
                    hacia(tortugas[i], tortugas[0])
                    tortugas[i].forward(radio2)
                    hacia(tortugas[i+1], tortugas[1])
                    tortugas[i+1].pencolor(random.choice(colores))
                    tortugas[i+1].forward(radio2)
            # t8.backward(radio)
            print("estoy en el segundo loop", k)
            #radio += 2
            #radio2 += 0.025
        ang1 += 9

    for i in range(9):
        tortugas[i].ht()

    miVentana.exitonclick()


main()
