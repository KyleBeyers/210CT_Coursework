##210CT LabTasks 7
##Task 1

class Vertex:
    def __init__(self, l):
        self.label = l
        self.neighbour = [] #holds list of neighbours 

    def addNeighbour(self, value):
        if value not in self.neighbour:
            self.neighbour.append(value)

class Graph:

    dictOfVertices = {} #dictionary to hold adjacency list
        
    def addVer(self, val):
        if isinstance(val,Vertex) and val.label not in self.dictOfVertices:
            self.dictOfVertices[val.label] = val
            print("Vertex added.")
            return True
        else:
            return False

    def addEdge(self, u, v):
        if u.label in self.dictOfVertices and v.label in self.dictOfVertices:
            for key, val in self.dictOfVertices.items():
                if key == u.label:
                    val.addNeighbour(v.label)
                if key == v.label:
                    val.addNeighbour(u.label)
            print("Edge added.")
            return True
        else:
            return False

    def display(self):
        v = self.dictOfVertices
        for vertex in (list(v.keys())):
            print(vertex + " -> " + str(v[vertex].neighbour))
        length = len(v)
        print("Graph has " + str(length) + " vertices.")

example = Graph()

v1 = Vertex("A")
v2 = Vertex("B")
v3 = Vertex("C")
v4 = Vertex("D")
example.addVer(v1)
example.addVer(v2)
example.addVer(v3)
example.addVer(v4)

example.addEdge(v1,v2)
example.addEdge(v1,v3)
example.addEdge(v2,v3)
example.addEdge(v3,v4)

example.display()

