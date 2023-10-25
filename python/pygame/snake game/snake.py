import turtle as t
class Snake:

    def __init__(self):
        self.box = []
        tim = t.Turtle("square")
        tim.penup()
        # tim.goto(-240, 0)
        self.box.append(tim)
        t.tracer(0)
        for i in range(0, 4):
            tam = t.Turtle("square")
            tam.color("white")
            tam.penup()
            self.box.append(tam)
            tam.goto(self.box[i].xcor() - 20, self.box[i].ycor())
        self.head = self.box[0]
        self.box[1].color("red")
    def extend(self):
        tam = t.Turtle("square")
        tam.color("white")
        tam.penup()
        self.box.append(tam)
        tam.goto(self.box[-1].xcor() - 20, self.box[-1].ycor())

        
    def move(self):
        
        for i in range(len(self.box) - 1, 0, -1):
            self.box[i].goto(self.box[i - 1].xcor(), self.box[i - 1].ycor())
        self.head.fd(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
   