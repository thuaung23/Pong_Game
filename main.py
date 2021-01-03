from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Score import Score
import time


# Set up playing board.
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddle on right and left.
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

# Create keys to move both paddles up and down.
screen.listen()
screen.onkey(right_paddle.upward, "Up")
screen.onkey(right_paddle.downward, "Down")
screen.onkey(left_paddle.upward, "q")
screen.onkey(left_paddle.downward, "a")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    # Ball bounces if it hits upper or lower wall.
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Ball bounces if it hits with either paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # If ball passes x_cor of 380 of right wall, left player gets a point.
    if ball.xcor() > 380:
        ball.reset_position()
        score.points_for_left()

    # If ball passes x_cor of -380 of left wall, right player gets a point.
    if ball.xcor() < -380:
        ball.reset_position()
        score.points_for_right()

    # In order to find out who wins, set a certain score limit.
    if score.left_score == 15:
        game_on = False
        score.winner(player="Left Player")

    elif score.right_score == 15:
        game_on = False
        score.winner(player="Right Player")

# To keep the board displaying.
screen.exitonclick()
