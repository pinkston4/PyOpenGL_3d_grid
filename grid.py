from OpenGL.GL import *


class MapGrid:
    """
    
    """
    def __init__(self):
        x = -5
        y = -5
        z = -5
        edge_x = 0
        vertices = ()
        edges = ()

        while x <= 5:
            while y <= 5:
                vertex = ((x, y, z,),)
                vertices = vertices + vertex
                y += 1
            x += 1
            y = -5
            # z += 1

        while edge_x < 120:
            point1 = edge_x
            point2 = edge_x + 1
            point3 = edge_x + 11
            edge1 = ((point1, point2,),)
            edge2 = ((point1, point3,),)
            edges = edges + edge1
            if edge_x <= 109:
                edges = edges + edge2
            # if edge_x < 90:
            #     point3 = point1 + 10
            #     point4 = point2 + 10
            #     edge2 = ((point3, point4,),)
            #     edges = edges + edge2
            edge_x += 1

        self.vertices = vertices
        self.edges = edges

    def draw_grid(self):
        """
        
        :return: 
        """
        glBegin(GL_LINES)
        for line in self.edges:
            for point in line:
                glVertex3fv(self.vertices[point])
        glEnd()
