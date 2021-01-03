from turtle import Turtle


class Paddle(Turtle):
    # Create paddles by using inheritance from Turtle class.
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def upward(self):
        # Only x_cor has to change to move up or down.
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def downward(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
