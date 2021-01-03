from turtle import Turtle


class Score(Turtle):
    # Create scoreboard from Turtle class.
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    # Update score according to given situations.
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    # Add points to the score of left player.
    def points_for_left(self):
        self.left_score += 1
        self.update_score()

    # Add points to the score of right player.
    def points_for_right(self):
        self.right_score += 1
        self.update_score()

    # Display who wins at the middle of the playing board.
    def winner(self, player):
        self.goto(0, 0)
        self.write(f"{player} Wins!", align="center", font=("Courier", 24, "normal"))