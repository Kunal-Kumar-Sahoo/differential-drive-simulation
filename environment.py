import pygame
import math


class Environment:
    def __init__(self, dimensions):
        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)

        # map dimensions
        self.height = dimensions[0]
        self.width = dimensions[1]

        # window settings
        pygame.display.set_caption('Differential Drive Robot')
        self.map = pygame.display.set_mode((self.width, self.height))

        # text variable
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.text = self.font.render('', True, self.white, self.black)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (dimensions[1]-600, dimensions[0]-100)

        # trail
        self.trail_set = list()

    def write_info(self, v_l, v_r, theta):
        text = f'V_l = {v_l} V_r = {v_r} Theta = {int(math.degrees(theta))}'
        self.text = self.font.render(text, True, self.white, self.black)
        self.map.blit(self.text, self.text_rect)

    def trail(self, position):
        for i in range(len(self.trail_set)-1):
            pygame.draw.line(
                self.map, self.yellow, 
                (self.trail_set[i][0], self.trail_set[i][1]), 
                (self.trail_set[i+1][0], self.trail_set[i+1][1]), 
                2
            )
        
        if self.trail_set.__sizeof__() > 30000:
            self.trail_set.pop(0)
        self.trail_set.append(position)

    def robot_frame(self, position, rotation):
        n = 80
        center_x, center_y = position
        
        x_axis = (center_x + n * math.cos(-rotation), center_y + n * math.sin(-rotation))
        y_axis = (center_x + n * math.cos(-rotation + math.pi / 2), center_y + n * math.sin(-rotation + math.pi / 2))

        pygame.draw.line(self.map, self.red, (center_x, center_y), x_axis, 3)
        pygame.draw.line(self.map, self.green, (center_x, center_y), y_axis, 3)