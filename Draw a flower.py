import turtle

wn= turtle.Screen()
wn.title("draw a flower")
wn.bgcolor("lightgreen")


t= turtle.Turtle()
def draw_flower():
    for i in range(4):
        t.pensize(5)
        t.color("orange","yellow")
        t.forward(200)
        t.begin_fill()
        t.circle(40,180)
        t.forward(200)
        t.left(90)
        t.end_fill()

draw_flower()





wn.mainloop()