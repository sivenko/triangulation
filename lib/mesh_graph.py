import bisect;
from vector import Vector
class Mesh:

    def __init__(self, *vertices):
        self.vertices = dict()
        if len(vertices) == 1 and isinstance(vertices[0], (list, tuple)):
            vertices = vertices[0]
        for vertex in vertices:
            self.vertices.setdefault(vertex, list())

    def get_edges(self, vertex):
        ''' (Mesha, Vertex)->(list of Vertex)

        Return a list of vertices which are connected to the given vertex
        '''
        return self.vertices[vertex]

    def iter_vertices(self, vertex):
        for v in self.vertices[vertex]:
            yield v.end
    
    def add_edge(self, vertex1, vertex2):
        bisect.insort(self.vertices[vertex1], Vector(vertex1, vertex2))
        bisect.insort(self.vertices[vertex2], Vector(vertex2, vertex1))

    def right_iter(self, around, left):
        base_vec = Vector(around, left)
        start_index, i, max_cos = None, 0, -2
        edges = []
        for edge in filter(lambda x: base_vec.is_cclockwise(x), self.vertices[around]):
            edges.append(edge)
            angle_cos = base_vec.cos_angle(edge)
            if angle_cos > max_cos:
                start_index, max_cos = i, angle_cos
            i = i + 1

        i, start_index = start_index, start_index - len(edges)
        while ( start_index < i):
            yield edges[i].end
            i = i - 1
        
    def left_iter(self, around, right):
        base_vec = Vector(around, right)
        start_index, i, max_cos = None, 0, -2
        edges = []
        for edge in filter(lambda x: base_vec.is_clockwise(x), self.vertices[around]):
            edges.append(edge)
            angle_cos = base_vec.cos_angle(edge)
            if angle_cos > max_cos:
                start_index, max_cos = i, angle_cos
            i = i + 1

        i = start_index - len(edges)
        while ( start_index > i):
            yield edges[i].end
            i = i + 1

    def join_vertices(self, *vertices):
        ''' (list of vertices)->None

        Creates full graph on specified vertices
        '''
        if len(vertices) == 1 and isinstance(vertices[0], (list, tuple)):
            vertices = vertices[0]
        edges_dict = self.vertices
  
        for i in range(len(vertices)-1):
            j = i + 1
            first_vertex_edges = edges_dict[vertices[i]]
            for k in range(j,len(vertices)):
                end_vertex_edges = edges_dict[vertices[k]]
                end_vertex = vertices[k]
                first_vertex_edges.append(vertices[k])
                end_vertex_edges.append(vertices[i])
                
    def lace_ccomponents(self, left_vertex, right_vertex):
        pass



