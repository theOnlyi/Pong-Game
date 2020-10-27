import pygame
from Ball import Ball
# from Paddle import paddle
from random import randint
from collections import namedtuple


def main():
    pygame.init()
    pygame.display.set_caption("My Pong")

    # creat a surface
    WIDTH = 800
    HEIGHT = 400
    BORDER = 20
    VELOCITY = 1
    FPS = 30  # frame rate
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    MyConstants = namedtuple("MyConstants", ["WIDTH", "HEIGHT", "BORDER", "VELOCITY", "FPS"])
    CONSTANTS = MyConstants(WIDTH, HEIGHT, BORDER, VELOCITY, FPS)

    # add solid background: r, g, b
    screen.fill((0, 0, 0))
    # double buffering: stage all the chages and update them at once
    # avoid flikering
    pygame.display.update()

    fgcolor = pygame.Color("Yellow")  # ball color
    bgcolor = pygame.Color("Black")  # background color

    # Draw walls as rectangles
    wcolor = pygame.Color("White")
    # top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    # pygame.display.update()
    # left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    # pygame.display.update()
    # bottom
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))
    # pygame.display.update()

    # ball init
    x0 = WIDTH - Ball.radius
    y0 = HEIGHT / 2
    vx0 = -VELOCITY
    vy0 = randint(-VELOCITY, VELOCITY)
    b0 = Ball(x0, y0, vx0, vy0, screen, fgcolor, bgcolor, CONSTANTS)
    b0.show(fgcolor)
    pygame.display.update()

    # define a variable to control the main loop
    running = True

    clock = pygame.time.Clock()

    # main loop
    while running:
        # event handling, get all event queue
        for event in pygame.event.get():
            # only do something if the event is of type Quit
            if event.type == pygame.QUIT:
                # quits the game
                running = False
            # if people dont close the window, update the postion of the ball
            pygame.display.update()
            clock.tick(FPS)
        # Ball movement:
        b0.update()


if __name__ == '__main__':
    main()
