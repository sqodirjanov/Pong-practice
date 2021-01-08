# Practicing game dev with classic pong

import turtle, winsound

# Game screen
window = turtle.Screen()
window.title("Practice Game - PoWg")
window.setup(width=800, height=600)
window.tracer(0)
window.bgcolor('black')


# Scoring
score_a = 0
score_b = 0


# Left Paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Right Paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 # 1/(10*(2**0.5))
ball.dy = 0.2 # 1/(10*(2**0.5))


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)



# Move paddle_a up and down
def paddle_a_up():
    y_coord = paddle_a.ycor()
    y_coord += 35
    paddle_a.sety(y_coord)


def paddle_a_down():
    y_coord = paddle_a.ycor()
    y_coord -= 35
    paddle_a.sety(y_coord)


# Move paddle_b up and down
def paddle_b_up():
    y_coord = paddle_b.ycor()
    y_coord += 35
    paddle_b.sety(y_coord)


def paddle_b_down():
    y_coord = paddle_b.ycor()
    y_coord -= 35
    paddle_b.sety(y_coord)


#Keybord binding
window.listen()
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_up, 'W')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_a_down, 'S')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')


# Main loop
while True:
    window.update()
    pen.clear()
    pen.write('Player A: ' + str(score_a) + '    Player B: ' + str(score_b), align='center', font=('Couruer', 24, 'normal'))
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check border
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
        # winsound.PlaySound(file_name.wav, winsound.SNDASYNC)
    
    if ball.xcor() > 400: 
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        # winsound.PlaySound(file_name.wav, winsound.SNDASYNC)


    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        # winsound.PlaySound(file_name.wav, winsound.SNDASYNC)
        

    # Check ball bounce off paddles
    if 350 > ball.xcor() > 340 and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.dx *= -1
        # winsound.PlaySound(file_name.wav, winsound.SNDASYNC)

    if -340 > ball.xcor() > -350 and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.dx *= -1
        # winsound.PlaySound(file_name.wav, winsound.SNDASYNC)
