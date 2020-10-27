import pygame
from Ball import Ball
# from Paddle import paddle
def main():
    pygame.init()
    pygame.display.set_caption("My Pong")

    # creat a surface
    WIDTH = 800
    HEIGHT = 400
    BOARDER = 20
    VELOCITY = 0.001
    FPS = 30 #frame rate
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # add solid background: r, g, b
    screen.fill((0, 0, 0))
    # double buffering: stage all the chages and update them at once
    # avoid flikering
    pygame.display.update()

    fgcolor = pygame.Color("White")
    bgcolor = pygame.Color("Black")

    # Draw walls as rectangles
    wcolor = pygame.Color("White")
    # top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BOARDER)))
    # pygame.display.update()
    # left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BOARDER, HEIGHT)))
    # pygame.display.update()
    # bottom
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT - BOARDER), (WIDTH, BOARDER)))
    # pygame.display.update()

    # ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT / 2
    vx0 = -VELOCITY
    vy0 = 0
    # TODO: +/- 45 degree random (calculate the random initilization)

    b0 = Ball(x0, y0, vx0, vy0, screen, fgcolor, bgcolor)
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

#TODO: push lab3 to git + capture a gif and include in README.md
