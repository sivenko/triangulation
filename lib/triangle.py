from operator import attrgetter,methodcaller
from vector import Vector

class InvalidNumberOfVertices(BaseException):
    pass
class Triangle:
    def __init__(self,  *vertices):
        '''(Triangle, array of vertices) -> (Triangle)

         inits new triangle object
         >>> tr = Triangle(Point(3,4), Point(2,5), Point(3,1))
         >>> [(p.x,p.y) for p in tr.vertices]
         [(2, 5), (3, 4), (3, 1)]
        '''
        if len(vertices) == 1 and isinstance(vertices[0], (list, tuple)):
            vertices = vertices[0]

        num_vertices = len(vertices)
        if num_vertices < 2 or num_vertices > 3 : 
            raise InvalidNumberOfVertices()
        else:
            self.vertices = vertices
            self.__restore_triangle()

        self.triangles = [self, self, self]

    def __str__(self):
        return '[{0}]'.format(','.join([str(v) for v in self.vertices]))

    def __restore_triangle(self):
        self.__order_vertices()
        self.__find_min_vertex()

    def __find_min_vertex(self):
        self.min_vertex = min(self.vertices, key=methodcaller('min_key'))

    def __order_vertices(self):
        vertices = self.vertices
        vertex_num = len(vertices)
        first_vertex = min(vertices, key=attrgetter('x','y'))
        vertices = list(vertices)
        vertices.remove(first_vertex)
        if vertex_num == 2:
            # dummy triangle, with two vertices
            self.vertices = [ first_vertex, vertices[0] ]
        else:
            # full triangle, three vertex
            if Vector(first_vertex, vertices[0]).is_clockwise(Vector(first_vertex, vertices[1])):
                self.vertices = [first_vertex, vertices[0], vertices[1]]
            else:
                self.vertices = [first_vertex, vertices[1], vertices[0]]

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

    def join_triangles(self, triangle):
        '''(Triangle, Triangle) -> (Triangle)

        Join two neigbour triangles if they have at least one common vertex
        in other case raises UnJoinableTriangles
        >>> tr1 = Triangle(Point(1,3), Point(3,3), Point(3,5))
        >>> tr2 = Triangle(Point(1,3), Point(3,3), Point(3,1))
        >>> tr1.join_triangle(tr2)
        >>> tr1.triangles[2] == tr2
        True
        >>> tr2.triangles[2] == tr1
        True
        '''
        self.__save_neighbour(triangle)
        triangle.__save_neighbour(self)
        return triangle

    def __save_neighbour(self, triangle):
        try:
            opposite_vertex = set(self.vertices).difference(triangle.vertices).pop()
        except InderError:
            # no difference, triangles are equal
            return
        vertex_index = self.vertices.index(opposite_vertex)
        next_vertex_index = (vertex_index + 1) % 3
        self.triangles[ vertex_index ] = triangle

        # next clockwise vertex should refer to the same triangle as updated one
        # if it's counter side doesn't have own neighbour triangle
        if self.triangles[next_vertex_index] == self:
            self.triangles[next_vertex_index] = triangle


    def add_vertex(self, vertex):
        if len(self.vertices) == 3:
            raise RuntimeError("Triangle already have 3 vertices")
        try:
            self.vertices.index(vertex)
            return
        except ValueError:
            # vertex is missed is ok to add it
            pass
        self.vertices.append(vertex)
        self.__restore_triangle()

    def __lt__ (self, triangle):
        if not isinstance(triangle, type(self)):
            raise TypeError("unorderable types: {0} > {1}".format(type(self), type(triangle)))
        if self.min_vertex.y < triangle.min_vertex.y:
            return True
        else:
            return False
        
if __name__ == '__main__':
    import doctest
    from vector import Point
    doctest.testmod()
