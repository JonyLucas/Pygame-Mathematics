from Mesh3D import *

class Cube3D(Mesh3D):
    def __init__(self):
        super().__init__()
        self.vertices = [
            (-0.5, -0.5, 0.5),
            (0.5, -0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, -0.5),
            (0.5, 0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5)
        ]

        self.triangles = [
            0, 2, 3, 0, 3, 1, # First Triangle: First Vertex, then First Vertex + 2, then First Vertex + 3 - Second Triangle: First Vertex, then First Vertex + 3, then First Vertex + 1
            2, 4, 5, 2, 5, 3,
            4, 6, 7, 4, 7, 5,
            6, 0, 1, 6, 1, 7,
            0, 2, 4, 0, 4, 6,
            1, 3, 5, 1, 5, 7
        ]