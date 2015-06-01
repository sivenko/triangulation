from operator import attrgetter
from graphics import Point
from math import ceil
class Set:
    def __init__(self, points):
        '''(Set, list of Points)->(Set)

        >>> s = Set((Point(1,3), Point(1,1), Point(0,6)))
        >>> [ (a.x, a.y) for a in s.points ]
        [(0, 6), (1, 1), (1, 3)]
        '''
        self.points = sorted(points, key=attrgetter('x','y'))

    def _triangulate(points, apply):
        size = len(points)
        if size <= 3:
            apply(points)
        else:
            mid = ceil(size / 2)
            Set._triangulate(points[0:mid], apply)
            Set._triangulate(points[mid:size], apply)

    def triangulate(self, apply):
        '''(self, function)->None

        >>> s = Set( (Point(1,1), Point(2,0), Point(2,3), Point(2,5), Point(3,1), Point(4,5), Point(5,3), Point(6,0), Point(6,1), Point(6,5)) )
        >>> s.triangulate(lambda x: print (' -> '.join([ '{0},{1}'.format(i.x, i.y) for i in x ]) ))
        1,1 -> 2,0 -> 2,3
        2,5 -> 3,1
        4,5 -> 5,3 -> 6,0
        6,1 -> 6,5
        '''
        Set._triangulate(self.points,apply)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
