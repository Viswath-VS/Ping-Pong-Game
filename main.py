import turtle
import winsound
# game window settings
window = turtle.Screen()
window.title("Pong game by Viswath")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#paddle 1 settings
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('square')
paddle_1.color('green')
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

#paddle 2 settings
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('square')
paddle_2.color('blue')
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

# game ball settings
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

# score card details
player_1=0
player_2=0
scoreCard = turtle.Turtle()
scoreCard.speed(0)
scoreCard.color("white")
scoreCard.hideturtle()
scoreCard.penup()
scoreCard.goto(0,260)
scoreCard.write("Player A:{}  Player B:{}".format(player_1,player_2),align="center",font=("Courier",24,"normal"))
# paddle upward movement function
def paddle_1_up():
    paddle_1.sety(paddle_1.ycor()+20)

def paddle_2_up():
    paddle_2.sety(paddle_2.ycor()+20)

# paddle downward movement function
def paddle_1_down():
    paddle_1.sety(paddle_1.ycor()-20)

def paddle_2_down():
    paddle_2.sety(paddle_2.ycor()-20)

# keyboard binding
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

#game main function loop
while True:
    window.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # top border settings
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # side boder settings
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        player_1 +=1
        scoreCard.clear()
        scoreCard.write("Player A: {}  Player B: {}".format(player_1,player_2),align="center",font=("Courier",24,"normal"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1 
        player_2 +=1
        scoreCard.clear()
        scoreCard.write("Player A: {}  Player B: {}".format(player_1,player_2), align="center",font=("Courier",24,"normal"))  

    # paddle and ball collision points
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor()<paddle_2.ycor()+50 and ball.ycor()>paddle_2.ycor()-50):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("sound.mp3",winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()<paddle_1.ycor()+50 and ball.ycor()>paddle_1.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("sound.mp3",winsound.SND_ASYNC)

    