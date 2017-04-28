import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from grid import MapGrid


class App(object):
    """
    class app 
    methods:
        __init__: initializes application, instantiates the grid and calls the
         looper method
        looper: looper contains the while loop that is this application
    """
    def __init__(self, screen_width, screen_height):
        """
        creates the scene, sets perspective, creates/instantiates grid, calls 
        looper
        :param screen_width: width of display
        :param screen_height: height of display
        """
        self.display = (screen_width, screen_height)
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        self.percpective = gluPerspective(45,
                                          (self.display[0]/self.display[1]),
                                          0.1, 50.0)
        self.step_back = glTranslatef(0.0, 0.0, -15)
        self.grid_map = MapGrid()
        self.looper()

    def looper(self):
        """
        the while loop that is the application, listens for quit event, rotates 
        and redraws the cube
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
    width, height = 1280, 720
    pygame.init()
    window = App(width, height)
