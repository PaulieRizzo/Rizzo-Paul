from vpython import *

ball = sphere(pos=vector(12, 0, 0), velocity=vector(0, 0, 0), radius=0.5, mass=1.0, color=color.cyan)  # Creates the ball
pivot = vector(0, 0, 0)  # Center or coordinate system
speed = vector(0.5, 0, 0)  # Change this to change speed
spring = helix(pos=pivot, velocity=speed, axis=ball.pos - pivot, radius=0.4, constant=1,
               thickness=0.1, coils=20, color=color.magenta)  # Creates the spring
hanger = box(pos=pivot, velocity=speed, color=color.yellow)  # Creates the block
eq = vector(9, 0, 0)  # Equilibrium position (how far away it would need to be away from spring to be at equilibrium)

earth_field = box(pos=vector(0, -1.5, 0), axis=vector(0, 0, 0), size=vector(20, 1, 10),
                  color=color.green)  # Creates the field

animation_time_step = 0.01  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.05
stop_time = 100.0  # This can be changed for a longer animation

time = 0
while time < stop_time:
    rate(rate_of_animation)

    acceleration = (eq - ball.pos) * (spring.constant / ball.mass)  # a = x * k / kg  (Similar to F=-k*x, although lacks mass)

    ball.velocity = ball.velocity + acceleration * time_step
    ball.pos = ball.pos + ball.velocity * time_step + spring.velocity * time_step  # Moves ball with spring

    spring.pos = spring.pos + spring.velocity * time_step  # Moves spring with given speed from earlier
    spring.axis = ball.pos - spring.pos

    hanger.pos = hanger.pos + hanger.velocity * time_step  # Moves block with given speed from earlier

    if hanger.pos.x > 2:  # Keeps it to a confined space
        spring.velocity = -spring.velocity
        hanger.velocity = -hanger.velocity

    if hanger.pos.x < -2:  # Keeps it to a confined space
        spring.velocity = -spring.velocity
        hanger.velocity = -hanger.velocity

    time += time_step
