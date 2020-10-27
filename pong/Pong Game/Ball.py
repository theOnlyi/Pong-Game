import pygame


class Ball:
    # pass
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor):
        # instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    # moving ball position
    def update(self):
        # new_position = old_position + difference delta position
        # delete the old ball
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)
        # TODO:
        # Check if Im collision (wall position):
            # flip the velocity

        # pass
