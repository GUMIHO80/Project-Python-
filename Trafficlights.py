import turtle 

turtle.setup(400,500)
wn= turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess= turtle.Turtle()


def draw_housing():
    tess.pensize(3)
    tess.color("black","darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40,180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.penup()
tess.forward(40)
tess.left(90)
tess.forward(50)
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

stateNum=0

def advance_state_machine():
    global stateNum
    canvas = turtle.getcanvas()
    x,y = canvas.winfo_pointerx(), canvas.winfo_pointery()
    print(x," ",y)

    if stateNum == 0: 
       tess.forward(70)
       tess.fillcolor("yellow")
       stateNum = 1
    elif stateNum == 1: 
       tess.forward(70)
       tess.fillcolor("red")
       stateNum = 2
    else: 
      tess.back(140)
      tess.fillcolor("green")
      stateNum = 0
    wn.ontimer(advance_state_machine, 3000 )
 
wn.onkey(advance_state_machine, "space")
wn.ontimer(advance_state_machine, 3000 )
wn.listen() 
wn.mainloop()