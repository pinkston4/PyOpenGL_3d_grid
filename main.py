import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from grid import MapGrid


class App(object):
    """
    
    """
    def __init__(self, screen_width, screen_height):
        self.display = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        self.percpective = gluPerspective(45,
                                          (self.display[0]/self.display[1]),
                                          0.1, 50.0)
        self.step_back = glTranslatef(0.0, 0.0, -20)
        self.grid_map = MapGrid()
        self.looper()

    def looper(self):
        """
        
        :return: 
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.grid_map.draw_grid()
            pygame.display.flip()
            pygame.time.wait(10)


if __name__ == "__main__":
    width, height = 800, 600
    pygame.init()
    window = App(width, height)