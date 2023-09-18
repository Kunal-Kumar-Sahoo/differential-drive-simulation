import pygame
import math


class Robot:
    def __init__(self, start_pos, robot_img, width):
        self.m2p = 3779.52 

        # robot dimensions
        self.width = width
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.theta = 0

        # velocities
        self.vl = 0.01 * self.m2p  
        self.vr = 0.01 * self.m2p  
        self.max_speed = 0.02 * self.m2p
        self.min_speed = -0.02 * self.m2p

        # graphics
        self.img = pygame.image.load(robot_img)
        self.rotated = self.img
        self.rect = self.rotated.get_rect(center=(self.x, self.y))

    def draw(self, map):
        map.blit(self.rotated, self.rect)

    def move(self, dt, event=None):
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.vl += 0.001 * self.m2p
                elif event.key == pygame.K_s:
                    self.vl -= 0.001 * self.m2p
                elif event.key == pygame.K_a:
                    self.vr += 0.001 * self.m2p
                elif event.key == pygame.K_d:
                    self.vr -= 0.001 * self.m2p
        
        self.x += ((self.vl + self.vr) / 2) * math.cos(self.theta) * dt
        self.y -= ((self.vl + self.vr) / 2) * math.sin(self.theta) * dt
        self.theta += (self.vr - self.vl) / self.width * dt

        # reset theta
        if self.theta > 2 * math.pi or self.theta < -2 * math.pi:
            self.theta = 0

        # set max speed
        self.vr = min(self.vr, self.max_speed)
        self.vl = min(self.vl, self.max_speed)

        # set min speed
        self.vr = max(self.vr, self.min_speed)
        self.vl = max(self.vl, self.min_speed)

        self.rotated = pygame.transform.rotozoom(self.img, math.degrees(self.theta), 1)
        self.rect = self.rotated.get_rect(center=(self.x, self.y))


