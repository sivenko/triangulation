from operator import attrgetter

class Point:
    def __init__(self, x, y):
        '''(Point, number, number) -> (Point)

        Returns Pint instanse identified by x and y coordinates
        >>> p = Point(3,4)
        >>> [p.x, p.y]
        [3, 4]
        '''
        self.x = x
        self.y = y

    def from_screen_point(point):
        '''(win.Point) -> (Point)'''
        assert False, 'not implemented yet'
        return Point(point.getX(), point.getY())

    def __str__(self):
        return 'x:{0}, y:{1}'.format(self.x, self.y)

    def __eq__(self, other):
        '''(Point, Point) -> (boolean)

        Rerturn true if points are equals, otherwise false
        >>> Point(1,3) == Point(1,3)
        True
        >>> Point(1,3) == Point(2,3)
        False
        >>> p1 = Point(1,3)
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
        '''
        '''
        return (hash(self.x) ^ hash(self.y) ^ hash((self.x, self.y)))

class Vector:
    def __init__(self, start_point, end_point):
        ''' (Vector, Point, Point) -> (Vector)

        Returns a vector instancse, identified by start and end point
        >>> vec = Vector(Point(1,2), Point(2,2))
        >>> [vec.x, vec.y]
        [1, 0]
        '''
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y

    def cross_product(self, vector):
        '''(Vector, Vector) -> (number)

        Returns cross product of two vectors
        >>> vec1 = Vector(Point(0,0), Point(3,2))
        >>> vec2 = Vector(Point(0,0), Point(2,3))
        >>> vec1.cross_product(vec2)
        5
        >>> vec2.cross_product(vec1)
        -5
        >>> vec1 = Vector(Point(0,0), Point(1,0))
        >>> vec2 = Vector(Point(0,0), Point(0,1))
        >>> vec1.cross_product(vec2)
        1
        >>> vec2.cross_product(vec1)
        -1
        '''
        return self.x * vector.y - self.y * vector.x

    def is_clockwise(self, vector):
        '''(Vector,Vector) -> (bool)

        Returns true if the second vector in clockwise position relativy to the first one
        >>> vec1 = Vector(Point(0,0), Point(1,0))
        >>> vec2 = Vector(Point(0,0), Point(0,1))
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
