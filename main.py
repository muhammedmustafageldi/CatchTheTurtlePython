import random
import turtle

gameBoard = turtle.Screen()

scoreTurtle = turtle.Turtle()
timerTurtle = turtle.Turtle()
gameOverTurtle = turtle.Turtle()
myTurtle = turtle.Turtle()

# Game Settings ->
maxCoordinateX = int(gameBoard.window_width() * 0.3)
maxCoordinateY = int(gameBoard.window_height() * 0.3)


print(maxCoordinateX)
print(maxCoordinateY)

leftTime = 15
score = 0


def setPropertiesOfScene():
    gameBoard.bgcolor('#DAF7A6')
    gameBoard.title("Catch The Turtle")


def setPropertiesOfTurtle():
    myTurtle.speed(0)
    myTurtle.shape('turtle')
    myTurtle.shapesize(2)
    myTurtle.color('red', '#FFC300')
    myTurtle.penup()

    gameOverTurtle.hideturtle()

    def handleClick(x, y):
        global score
        score += 1
        print(x, y)
        updateAndWriteScore()

    myTurtle.onclick(handleClick)


def countDownTimer():
    global leftTime

    timerTurtle.speed(0)
    timerTurtle.hideturtle()
    timerTurtle.penup()

    timerTurtle.clear()
    timerTurtle.goto(0, 290)
    timerTurtle.write(f"Time: {leftTime}", align="center", font=("Arial", 24, "bold"))
    leftTime -= 1

    if leftTime > 0:
        changeThePosition()
        turtle.ontimer(countDownTimer, 500)
    else:
        scoreTurtle.clear()
        timerTurtle.clear()
        myTurtle.hideturtle()

        gameOverTurtle.hideturtle()
        gameOverTurtle.speed(0)
        gameOverTurtle.clear()
        gameOverTurtle.penup()
        gameOverTurtle.goto(0, 0)
        gameOverTurtle.write(f"Game over! Your score: {score}", align="center", font=("Arial", 24, "bold"))


def updateAndWriteScore():
    global score

    scoreTurtle.hideturtle()
    scoreTurtle.speed(0)
    scoreTurtle.clear()
    scoreTurtle.penup()
    scoreTurtle.goto(0, 320)
    scoreTurtle.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))


def changeThePosition():
    global maxCoordinateY
    global maxCoordinateX

    randomX = random.randint(-maxCoordinateX, maxCoordinateX)
    randomY = random.randint(-maxCoordinateY, maxCoordinateY)

    print(randomX)
    print(randomY)

    myTurtle.goto(randomX, randomY)


def startGame():
    turtle.tracer(0)
    setPropertiesOfScene()
    setPropertiesOfTurtle()
    updateAndWriteScore()
    countDownTimer()
    turtle.tracer(1)


startGame()
turtle.mainloop()
