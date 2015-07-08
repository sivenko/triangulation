import unittest
from mesh_graph import Mesh
from vector import Vertex
import pprint
class CreateMesh(unittest.TestCase):

    def test_mesh_with_vertices(self):
        v1, v2, v3 = Vertex(1,2), Vertex(3,5), Vertex(3,6)
        mesh = Mesh(v1, v2, v3)
        self.assertListEqual([mesh.vertices[v] for v in [v1,v2,v3]], [[],[],[]])
        self.assertEqual(len(mesh.vertices), 3)

class JoinVertices(unittest.TestCase):
    def test_join_vertices(self):
        v1, v2, v3, v4, v5 = Vertex(1,2), Vertex(3,5), Vertex(3,6), Vertex(1,1), Vertex(2,3)
        mesh = Mesh(v1, v2, v3, v4, v5)
        mesh.join_vertices(v1, v2, v3, v4, v5)
        self.assertSetEqual(set(mesh.get_edges(v1)), set((v2, v3, v4, v5)))
        self.assertSetEqual(set(mesh.get_edges(v2)), set((v1, v3, v4, v5)))
        self.assertSetEqual(set(mesh.get_edges(v3)), set((v1, v2, v4, v5)))
        self.assertSetEqual(set(mesh.get_edges(v4)), set((v1, v2, v3, v5)))
        self.assertSetEqual(set(mesh.get_edges(v5)), set((v1, v2, v3, v4)))

class IterEdges(unittest.TestCase):
    def test_left_iter(self):
        centr, right, v1, v2, v3, v4, v5 =\
                Vertex(1,1), Vertex(4,1), Vertex(0,3), Vertex(1,2), Vertex(3,2), Vertex(0,0), Vertex(2,0)

        mesh = Mesh(centr, right, v1, v2, v3, v4, v5)
        for v in (v1, v2, v3, v4, v5):
            mesh.add_edge(centr, v)

        vertices = mesh.left_iter(centr, right)
        expected = [v3, v2, v1];
        got = [v for v in vertices]
        self.assertListEqual(got, expected)

    def test_right_iter(self):
        centr, left, v1, v2, v3, v4, v5 =\
                Vertex(1,1), Vertex(-1,1), Vertex(0,3), Vertex(1,2), Vertex(3,2), Vertex(0,0), Vertex(2,0)

        mesh = Mesh(centr, left, v1, v2, v3, v4, v5)
        for v in (v1, v2, v3, v4, v5):
            mesh.add_edge(centr, v)

        vertices = mesh.right_iter(centr, left)
        expected = [v1, v2, v3];
        got = [v for v in vertices]
        print("got")
        for v in got:
            print (str(v))
        print("exp")
        for v in expected:
            print (str(v))
        self.assertListEqual(got, expected)

class LaceCComponents(unittest.TestCase):
    pass

if __name__ == '__main__':
   unittest.main()

