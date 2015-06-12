from operator import attrgetter

class Vertex:
    def __init__(self, x, y):
        '''(Vertex, number, number) -> (Vertex)

        Returns Vertex instanse identified by x and y coordinates
        >>> p = Vertex(3,4)
        >>> [p.x, p.y]
        [3, 4]
        '''
        self.x = x
        self.y = y
        self.edges = list()

    def min_key(self):
        return (self.y, -self.x)

    def add_neigbour(vertex):
        '''(Vertex, Vertex) -> None

        Adds neigbour vertex, stored in clockwise order to the self vertex
        >>> p1, p2, p3 = Vertex(3,4), Vertex(3,5), Vertex(3,1)
        >>> p1.add_neigbour(p2,p3);
        None
        '''


    def from_screen_vertex(vertex):
        '''(win.Vertex) -> (Vertex)'''
        assert False, 'not implemented yet'
        return Vertex(vertex.getX(), vertex.getY())

    def __str__(self):
        return '({0},{1})'.format(self.x, self.y)

    def __eq__(self, other):
        '''(Vertex, Vertex) -> (boolean)

        Rerturn true if vertexs are equals, otherwise false
        >>> Vertex(1,3) == Vertex(1,3)
        True
        >>> Vertex(1,3) == Vertex(2,3)
        False
        >>> p1 = Vertex(1,3)
        >>> p2 = p1
        >>> p2 == p1
        True
        '''
        if isinstance(other, type(self)) \
                and self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __hash__(self):
        return (hash(self.x) ^ hash(self.y) ^ hash((self.x, self.y)))

    def rightmost_triangle(self):
        pass

    def leftmost_triangle(self):
        pass

class Vector:
    def __init__(self, start_vertex, end_vertex):
        ''' (Vector, Vertex, Vertex) -> (Vector)

        Returns a vector instancse, identified by start and end vertex
        >>> vec = Vector(Vertex(1,2), Vertex(2,2))
        >>> [vec.x, vec.y]
        [1, 0]
        '''
        self.x = end_vertex.x - start_vertex.x
        self.y = end_vertex.y - start_vertex.y

    def cross_product(self, vector):
        '''(Vector, Vector) -> (number)

        Returns cross product of two vectors
        >>> vec1 = Vector(Vertex(0,0), Vertex(3,2))
        >>> vec2 = Vector(Vertex(0,0), Vertex(2,3))
        >>> vec1.cross_product(vec2)
        5
        >>> vec2.cross_product(vec1)
        -5
        >>> vec1 = Vector(Vertex(0,0), Vertex(1,0))
        >>> vec2 = Vector(Vertex(0,0), Vertex(0,1))
        >>> vec1.cross_product(vec2)
        1
        >>> vec2.cross_product(vec1)
        -1
        '''
        return self.x * vector.y - self.y * vector.x

    def is_clockwise(self, vector):
        '''(Vector, Vector) -> (bool)

        Returns true if the second vector in clockwise position relativy to the first one
        >>> vec1 = Vector(Vertex(0,0), Vertex(1,0))
        >>> vec2 = Vector(Vertex(0,0), Vertex(0,1))
        >>> vec1.is_clockwise(vec2)
        False
        >>> vec2.is_clockwise(vec1)
        True
        >>> vec1.is_clockwise(vec1)
        True
        '''
        if self.cross_product(vector)  > 0:
            return False
        else:
            return True
    
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
