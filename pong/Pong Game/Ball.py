import pygame


class Ball:
    # pass
    radius = 10

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor, constants):
        # instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.constants = constants

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.radius)

    # moving ball position
    def update(self):
        # new_position = old_position + difference delta position
        # delete the old ball
        self.show(self.bgcolor)

        # Check if Im collision (wall position):
        # flip the velocity
        posi_x = self.x + self.vx
        posi_y = self.y + self.vy
        if posi_x < (self.constants.BORDER + self.radius):
            self.vx = -self.vx
        if posi_y < (self.constants.BORDER + self.radius):
            self.vy = -self.vy
        if posi_y > (self.constants.HEIGHT - self.radius - self.constants.BORDER):
            self.vy = -self.vy
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)
        # pass
