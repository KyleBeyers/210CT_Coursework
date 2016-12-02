##210CT LabTasks 7
##Task 1 pseudocode

class Vertex:
    DEF __INIT__(SELF, L):
        label <- l
        neighbour <- []

    DEF ADDNEIGHBOUR(SELF, VALUE):
        if value is not in neighbour then:
            add value to neighbour list

class Graph:

    dictOfVertices <- {}
    
    DEF __INIT__(SELF):
        graph length <- 0
        
    DEF ADD_VER(SELF, VAL):
        if val is an instance of Vertex and vertex label not in dictOfVertices then:
            add value into dictOfVertices
            output "Vertex added."
            return True
        else:
            return False

    DEF ADD_EDGE(SELF,U,V):
        if u and v is in dictOfVertices:
            assign value v to key u
            assign value u to key v
            output "Edge added."
            return True
        else:
            return False

    DEF DISPLAY(SELF):
        for vertex in dictOfVertices keys:
            output vertex with neighbours to it
        length <- length of dictOfVertices
        output graph length
