from operator import attrgetter
from vector import Vector
class InvalidNumberOfPoint(BaseException):
    pass
class Triangle:
    def __init__(self,  *vertices):
        '''(Triangle, array of vertices) -> (Triangle)

         inits new triangle object
         >>> tr = Triangle(Point(3,4), Point(2,5), Point(3,1))
         >>> [(p.x,p.y) for p in tr.vertices]
         [(2, 5), (3, 4), (3, 1)]
        '''
        num_vertices = len(vertices)
        if num_vertices < 2 or num_vertices > 3 : 
            raise InvalidNumberOfVertices()
        else:
            first_vertex = min(vertices, key=attrgetter('x','y'))
            vertices = list(vertices)
            vertices.remove(first_vertex)
            if num_vertices == 2:
                self.vertices = [ first_vertex, vertices[0] ]
            else: # full triangle, three vertex
                if Vector(first_vertex, vertices[0]).is_clockwise(Vector(first_vertex, vertices[1])):
                    self.vertices = [first_vertex, vertices[0], vertices[1]]
                else:
                    self.vertices = [first_vertex, vertices[1], vertices[0]]
        
        self.triangles = [self, self, self]

    def iter_clockwise(self, triangle):
        '''(Triangle, Triangle or int) -> (generator)
        Creates triangle iterator, which iterates through self.triangles
        starting from triangle in clockwise order
        '''
        if isinstance(triangle, int):
            i = triangle
        elif isinstance(triangle, Triangle):
            i = self.triangles.index(triangle)
        else:
            raise ValueError('Unsupported type {1}'.format(x.__class__.__name__))
        n = len(self.triangles)
        for tr in range(n):
            c, i = i, (i+1)%n
            yield self.triangles[c]

    def add_triangle(self, triangle):
        '''(Triangle, array of vertices) -> (Triangle)

        Create a new triangle from set of vertices and add's it
        to the current triangle. Returns new created Triangle
        >>> tr1 = Triangle(Point(1,3), Point(3,3), Point(3,5))
        >>> tr2 = Triangle(Point(1,3), Point(3,3), Point(3,1))
        >>> tr1.add_triangle(tr2)
        >>> tr1.triangles[2] == tr2
        True
        >>> tr2.triangles[2] == tr1
        True
        '''
        self._save_neighbour(triangle)
        triangle._save_neighbour(self)

    def _save_neighbour(self, triangle):
        opposite_vertex = set(self.vertices).difference(triangle.vertices).pop()
        vertex_index = self.vertices.index(opposite_vertex)
        next_vertex_index = (vertex_index + 1) % 3
        self.triangles[ vertex_index ] = triangle

        # next clockwise vertex should refer to the same triangle as updated one
        # if it's counter side doesn't have own neighbour triangle
        if self.triangles[next_vertex_index] == self:
            self.triangles[next_vertex_index] = triangle
        
if __name__ == '__main__':
    import doctest
    from vector import Point
    doctest.testmod()
