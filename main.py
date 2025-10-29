# type: ignore

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

gravity = 1  
friction = 0.8  

colors_array = ["red", "blue", "purple", "yellow", "cyan", "green"]

def random_int_from_range(min_val, max_val):
    return random.randint(min_val, max_val)

class Ball:
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def update(self):
        if self.y + self.radius + self.dy > HEIGHT:
            self.dy = -self.dy * friction
        else:
            self.dy += gravity

        if self.x + self.radius + self.dx > WIDTH or self.x - self.radius <= 0:
            self.dx = -self.dx

        self.x += self.dx
        self.y += self.dy

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

ballArray = []

def init():
    global ballArray
    ballArray = []
    for _ in range(200):
        radius = random_int_from_range(10, 30)
        x = random_int_from_range(radius, WIDTH - radius)
        y = random_int_from_range(radius, HEIGHT - radius)
        dx = random_int_from_range(-10, 10)
        dy = random_int_from_range(-10, 10)
        color = random.choice(colors_array)
        ballArray.append(Ball(x, y, dx, dy, radius, color))

def draw():
    screen.clear()
    for ball in ballArray:
        ball.draw()

def update():
    for ball in ballArray:
        ball.update()

def on_mouse_down():
    init() 

init()
pgzrun.go()