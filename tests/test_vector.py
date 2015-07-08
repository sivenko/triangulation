import unittest
from vector import Vector, Vertex
class TestVector(unittest.TestCase):

    def test_empty_vector(self):
        v = Vector()
        self.assertTupleEqual((v.x, v.y, v.start, v.end), (None, None, None, None))

    def test_vector(self):
        start, end = Vertex(1,0), Vertex(4,5)
        vector = Vector(start, end)

        self.assertListEqual([vector.start, vector.end], [start, end])
        self.assertListEqual([vector.x, vector.y], [end.x - start.x, end.y - start.y]) 

    def test_left_orthogonal(self):
        start, end = Vertex(0,0), Vertex(2,1)
        vector = Vector(start, end)
        ort_vector = vector.left_orthogonal()
        
        self.assertListEqual([ort_vector.x, ort_vector.y], [ -1, 2])
        self.assertListEqual([ort_vector.start, ort_vector.end], [ start, Vertex(-1, 2)])

    def test_clockwise(self):
        start = Vertex(2,1)
        base_vector = Vector(start, Vertex(3,1))
        clockwise = ((3,2),(2,2),(1,2))
        not_clockwise = ((1,1),(1,0),(2,0),(3,0),(3,1))
        self.assertListEqual([base_vector.is_clockwise(Vector(start, Vertex(v[0],v[1]))) for v in clockwise], [True for x in range(len(clockwise))])
        self.assertListEqual([base_vector.is_clockwise(Vector(start, Vertex(v[0],v[1]))) for v in not_clockwise], [False for x in range(len(not_clockwise))])

    def test_cclockise(self):
        start = Vertex(2,1)
        base_vector = Vector(start, Vertex(3,1))
        cclockwise = ((1,0),(2,0),(3,0))
        not_cclockwise = ((1,1),(3,2),(2,2),(1,2),(3,1))
        self.assertListEqual([base_vector.is_cclockwise(Vector(start, Vertex(v[0],v[1]))) for v in cclockwise], [True for x in range(len(cclockwise))])
        self.assertListEqual([base_vector.is_cclockwise(Vector(start, Vertex(v[0],v[1]))) for v in not_cclockwise], [False for x in range(len(not_cclockwise))])

        
if __name__ == '__main__':
   unittest.main()
