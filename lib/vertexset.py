from operator import attrgetter
from math import ceil
from triangle import Triangle
import numpy

class Set:
    def __init__(self, vertices):
        '''(Set, list of Points)->(Set)

        >>> s = Set((Point(1,3), Point(1,1), Point(0,6)))
        >>> [ (a.x, a.y) for a in s.vertices ]
        [(0, 6), (1, 1), (1, 3)]
        '''
        self.vertices = sorted(vertices, key=attrgetter('x','y'))

    def triangulate(vertices, apply):
        size = len(vertices)
        if size <= 3:
            return Triangle(vertices)
        else:
            mid = ceil(size / 2)
            tr1 = Set.triangulate(vertices[0:mid], apply)
            tr2 = Set.triangulate(vertices[mid:size], apply)

class SubSet:
    def __init__(self, vertices, min_vertex= None):
        if min_vertex,
        self.bottom_vertex = min(vertices, key=attrgetter('y','__minus_x'))
        self.vertices = vertices

        tr = Triangle(vertices)
        self.triangle = tr

    def merge(right_set, left_set):
        right_min_vertex = right_set.bottom_vertex
        left_min_vertex = left_set.bottom_vertex
        merged_min_vertex = min((right_min_vertex, left_min_vertex), key=attrgetter('y','__minus_x'))
        merged_set = n
        merge_triangle = Triangle(right_min_vertex, left_min_vertex)
        while True:
            right_candidate = right_set.find_right_candidate(right_min_vertex)
            left_candidate = left_set.find_left_candidate(left_min_vertex)
            if right_candidate != None and \
                    (left_candidate == None or not in_circle(right_candidate, left_min_vertex, right_min_vertex, left_candidate)):
                right_min_vertex = right_candidate
                merge_triangle = add_new_vertex(merge_triangle, left_min_vertex, right_min_vertex)
            elif left_candidate != None:
                left_min_vertex = left_candidate
                merge_triangle = add_new_vertex(merge_triangle, right_min_vertex, left_min_vertex)
            else:
                # no candidates merge is completed
                break
        return

    def find_right_candidate(self, right_min_vertex):
        right_candidates = right_min_vertex.right_candidates()
        triangulation_vertex = None
        try:
            candidate_vertex = next(right_candidates)
            while candidate_vertex != None:
                if Vector(right_vertex, left_vertex).check_angle(right_vertex, candidate_vertex):
                    next_candidate_vertex = next(right_candidates)
                    if inCircle(left_vertex, right_vertex, candidate_vertex, next_candidate_vertex):
                        candidate_vertex = next_candidate_vertex
                    else:
                        triangulation_vertex = candidate_vertex
                        break
                else:
                    break
        except StopIteration:
            pass

    def add_vertex(triangle, old_lr_point, new_lr_point):
        triangle.add_vertex(new_lr_point)
        return Triangle(old_lr_point, new_lr_point)

    def in_cirle(vertex1, vertex2, vertex3, vertex4):
        '''(Vertex, Vertex, Vertex, Vertex) -> (bool)

        Returns true if vertex4 lies in circle defined by vertex1, vertex2, vertex3
        Precondition: triangle defined by vertex1, vertex2, vertex3
        should be on the left to the vertex4
        '''

        if vertex1 == None:
            return False
        if vertex4 == None:
            return True
        else:
            m = [
                    [vertex1.x, vertex1.y, vertex1.x**2 + vertex1.y**2, 1],
                    [vertex2.x, vertex2.y, vertex2.x**2 + vertex2.y**2, 1],
                    [vertex3.x, vertex3.y, vertex3.x**2 + vertex3.y**2, 1],
                    [vertex4.x, vertex4.y, vertex4.x**2 + vertex4.y**2, 1],
                ]

            det = numpy.linalg.det(m)
            if det > 0:
                return True
            else:
                return False:

if __name__ == '__main__':
    import doctest
    from graphics import Point
    doctest.testmod()
