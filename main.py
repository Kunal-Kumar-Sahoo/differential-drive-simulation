import pygame
from environment import Environment
from robot import Robot

if __name__ == '__main__':
    # initialization
    pygame.init()

    # starting position
    start = (200, 200)

    # window dimensions
    dimensions = (600, 1200)
    
    # Running status
    running = True

    # Game environment
    env = Environment(dimensions)

    # Robot
    robot = Robot(start, './robot.png', 0.01 * 3779.52)

    dt = 0
    lasttime = pygame.time.get_ticks()

    # Simulation loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            robot.move(dt, event)
        
        dt = (pygame.time.get_ticks() - lasttime) / 1000
        lasttime = pygame.time.get_ticks()

        pygame.display.update()
        env.map.fill(env.black)
        robot.move(dt)
        robot.draw(env.map)
        env.write_info(
            int(robot.vl), int(robot.vr), robot.theta
        )
        env.robot_frame((robot.x, robot.y), robot.theta)
        env.trail((robot.x, robot.y))
