from OpenGL.GL import *


class MapGrid:
    """
    
    """
    def __init__(self):
        """
        
        """
        x = -5
        y = -5
        z = -5
        edge_x = 0
        vertices = ()
        edges = ()

        while z <= 5:

            while x <= 5:
                while y <= 5:
                    vertex = ((x, y, z,),)
                    vertices = vertices + vertex
                    y += 1
                x += 1
                y = -5
            x = -5
            y = -5
            z += 1

            while edge_x < 1330:
                point1 = edge_x
                point2 = edge_x + 1
                point3 = edge_x + 11
                point4 = edge_x + 121

                edge1 = ((point1, point2,),)
                edge2 = ((point1, point3,),)
                edge3 = ((point1, point4,),)

                edges = edges + edge1

                if edge_x < 109:
                    edges = edges + edge2

                if edge_x < 1209:
                    edges = edges + edge3

                edge_x += 1


        self.vertices = vertices
        self.edges = edges
        # self.surface = (0, 10, 110, 120)
        # self.color = (0, 1, 0)

    def draw_grid(self):
        """
        
        :return: 
        """
        # glBegin(GL_QUADS)
        #
        # for vertex in self.surface:
        #     glColor3fv(self.color)
        #     glVertex3fv(self.vertices[vertex])
        #
        # glEnd()

        glBegin(GL_LINES)
        for line in self.edges:
            for point in line:
                glVertex3fv(self.vertices[point])
        glEnd()
