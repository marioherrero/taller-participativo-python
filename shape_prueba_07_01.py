import turtle
import math
import random

t0 = turtle.Turtle()
t0.speed(0)
t0.penup()
t1 = turtle.Turtle()
t1.speed(0)
t1.penup()
miVentana = turtle.Screen()
miVentana.bgcolor("black")
ang2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
p = 25
poligono = ((1, p), (-1, p), (-10, 0), (0, -5), (10, 0))
miVentana.register_shape("poligono", poligono)
t0.shapesize(outline=1)
t0.shape("poligono")
t1.shapesize(outline=6)
t1.shape("poligono")
puntos = []
filas = 21
columnas = 21
yy = 300
for i in range(filas):
    puntos_aux = []
    xx = -300
    for j in range(columnas):
        puntos_aux.append((xx, yy))
        xx += 30
    puntos.append(puntos_aux)
    yy -= 30
t0.pencolor("maroon")
for i in range(filas):
    for j in range(columnas):
        t0.goto(puntos[i][j])

colores = [["gold", "olive", ], ["brown", "maroon"],
           ["darkorange",  "gold"], ["maroon", "orange"],
           ["olive", "gold"], ["maroon", "darkorange"],
           ["chocolate", "olive"], ["red", "olive"], ["red", "darkgreen"]]
camino = []
for j in range(11):
    for i in range(21-j*2):
        camino.append([20-j, i+j])
    k = 19-j
    for i in range(20-j*2):
        camino.append([k, 20-j])
        k -= 1
    k = 19-j
    for i in range(20-j*2):
        camino.append([0+j, k])
        k -= 1
    k = 1+j
    for i in range(19-j*2):
        camino.append([k, 0+j])
        k += 1


def angulo(t1, t2):  # ingresan dos objetos tortugas como datos
    ang = math.degrees(math.atan2(t2.ycor()-t1.ycor(), t2.xcor()-t1.xcor()))
    #print("ang=", ang)
    return ang


def ir_a(ang, i, j):
    if ang > -22.5 and ang < 22.5:
        j += 1
        # print("ir_a j+1=", j)
    if ang > 22.5 and ang < 67.5:
        i -= 1
        j += 1
        # print("ir_a i-1=", i, "j+1=", j)
    if ang > 67.5 and ang < 112.5:
        i -= 1
        # print("ir_a i-1=", i)
    if ang > 112.5 and ang < 157.5:
        i -= 1
        j -= 1
        # print("ir_a i-1=", i, "ir_a j-1=", j)
    if ang > 157.5 and ang <= 180 or ang < -180 and ang < -157:
        j -= 1
        # print("ir_a i=", i, "ir_a j-1=", j)
    if ang > -157.5 and ang < -112.5:
        i += 1
        j -= 1
    if ang > -112.5 and ang < -67.5:
        i += 1
    if ang > -67.5 and ang < -22.5:
        i += 1
        j += 1
    return i, j


def main():
    t1.pencolor("green")
    t1.pensize(1)
    t1.shapesize(outline=2)
    i0 = camino[0][0]
    j0 = camino[0][1]
    camino_t1 = []
    angulos = []
    i1 = 15
    j1 = 20
    t1.goto(puntos[i1][j1])
    camino_t1.append(t1.pos())
    angulos.append(angulo(t1, t0))
    #t1.dot(10, "green")
    t0.ht()
    # t0.pendown()
    t0.pencolor("red")
    ang1 = 140
    p = 90
    for j in range(1):
        i1 = 8
        j1 = 4
        t1.goto(puntos[i1][j1])
        t0.shape("poligono")
        for i in range(len(camino)):
            poligono = ((1, p), (-1, p), (-10, 0), (0, -5), (10, 0))
            miVentana.register_shape("poligono", poligono)
            t0.shapesize(outline=0.5)
            t0.shape("poligono")
            i0 = camino[i][0]
            j0 = camino[i][1]
            t0.goto(puntos[i0][j0])
            for k in range(2):
                color = random.choice(colores)
                t1.color(color[0], color[1])
                t1.seth(angulo(t1, t0))
                t1.forward(8)
                t1.right(ang1+random.choice(ang2))
                t1.stamp()
                ang1 -= 0.18
            p -= 0.05

    miVentana.exitonclick()


main()
