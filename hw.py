#Ship moves wawardly, and box bounces from corner to corner
import pgzrun, random, itertools

#Setup
WIDTH = 800
HEIGHT = 800

#Positions
BALL_POSITIONS = [(700, 100), (100, 700), (700, 700), (100, 100)]
ball_positions = itertools.cycle(BALL_POSITIONS)
50
#Crate actors
ball = Actor("basketball", center = (50, 50))

#Draw function
def draw():
    screen.clear()
    ball.draw()

#Moving the ball
def move_ball():
    animate(ball, "bounce_end", duration = 1, pos = next(ball_positions))

#Continue to move ball
clock.schedule_interval(move_ball, 1)

pgzrun.go()