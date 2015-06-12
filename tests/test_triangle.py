import unittest
from triangle import Triangle
from vector import Vertex
from itertools import chain

class CreateTriangle(unittest.TestCase):
    
    def test_new_triangle(self):
        p1, p2, p3 = Vertex(2, 5), Vertex(3, 1), Vertex(3, 4)
        tr = Triangle(p1, p2, p3)
        got = list(chain.from_iterable((p.x, p.y) for p in tr.vertices)) 
        expected = [2, 5, 3, 4, 3, 1]
        self.assertListEqual(got, expected, 'vertices init order')
        self.assertListEqual(tr.triangles, [tr, tr, tr], 'neighbor triangles init')
    
    def test_iter(self):
        p1, p2, p3, p4, p5 = Vertex(2,5), Vertex(3, 1), Vertex(3, 4), Vertex(5, 2), Vertex(5, 6)
        tr1, tr2, tr3 = Triangle(p1, p2, p3), Triangle(p2, p3, p4), Triangle(p3, p4, p5)
        # FIXME: use add_triangles to form the list
        tr2.triangles = [tr1, tr2, tr3]
        iterator = tr2.iter_clockwise(tr2)
        self.assertEqual(tr2, next(iterator))
        self.assertEqual(tr3, next(iterator))
        self.assertEqual(tr1, next(iterator))

        iterator = tr2.iter_clockwise(2)
        self.assertEqual(tr3, next(iterator))
        self.assertEqual(tr1, next(iterator))
        self.assertEqual(tr2, next(iterator))

        
    def test_join_triangles(self):
        p1, p2, p3, p4 = Vertex(1,3), Vertex(3,3), Vertex(3,5), Vertex(3,1)
        tr1 = Triangle(p1, p2, p3)
        tr2 = Triangle(p1, p2, p4)
        tr1.join_triangles(tr2)

        tr2_index = tr1.vertices.index(p3)
        tr_iter = tr1.iter_clockwise(tr2_index)
        self.assertEqual(next(tr_iter), tr2)
        self.assertEqual(next(tr_iter), tr2)
        self.assertEqual(next(tr_iter), tr1)

        tr1_index = tr2.vertices.index(p4) 
        tr_iter = tr2.iter_clockwise(tr1_index)
        self.assertEqual(next(tr_iter), tr1)
        self.assertEqual(next(tr_iter), tr1)
        self.assertEqual(next(tr_iter), tr2)

    def test_add_vertex(self):
        p1, p2, p3 = Vertex(1,3), Vertex(3,4), Vertex(3,5)
        etalon = [ p1, p3, p2 ]
        tr1 = Triangle (p1, p3)
        tr1.add_vertex(p2)
        self.assertListEqual(tr1.vertices, etalon)

        tr1 = Triangle(p2, p3)
        tr1.add_vertex(p1)
        self.assertListEqual(tr1.vertices, etalon)

        tr1 = Triangle(p3, p1)
        tr1.add_vertex(p1)
        self.assertListEqual(tr1.vertices, [p1, p3])

if __name__ == '__main__':
   unittest.main()

