#Ship moves wawardly, and box bounces from corner to corner
import pgzrun, random, itertools

#Setup
WIDTH = 400
HEIGHT = 400

#Positions
BLOCK_POSITIONS = [(350, 50), (350, 350), (50, 350), (50,  50)]
block_positions = itertools.cycle(BLOCK_POSITIONS)

#Crate actors
ship = Actor("spaceship", center = (200,200))
block = Actor("box", center = (50, 50))

#Draw function
def draw():
    screen.clear()
    ship.draw()
    block.draw()

#Moving the block
def move_block():
    animate(block, "bounce_end", duration = 1, pos = next(block_positions))

#Continue to move block
clock.schedule_interval(move_block, 1)

#Randomly giving ship a target
def next_ship_target():
    x = random.randint(100,300)
    y = random.randint(100, 300)
    ship.target = x,y
    target_angle = ship.angle_to(ship.target)
    target_angle += 360 * ((ship.angle - target_angle + 180) // 360)
    animate(ship, angle = target_angle, duration = 0.3, on_finished = move_ship)

#Moving ship
def move_ship():
    animate(ship, tween = "accel_decel", pos = ship.target, duration = ship.distance_to(ship.target) / 200, on_finished = next_ship_target)

#Calling the function
next_ship_target()
pgzrun.go()