# Multiple ways to build graphs
# 1) Edge list - build a graph using a list of connected nodes via their edges
# Ex. graph = [[0,2], [2,3], [2,1], [1,3]]

# 2) Adjacent List - index = the node and the list at that index are the nodes that node is connected to
# Ex. graph = [[2], [2,3], [0,1,3], [1,2]]

# 3) Adjacent Matrix - matrix that has 0 and 1s. 0 = no connection @ that location, 1 = connection
# Ex. graph = [
#   [0, 0, 1, 0], (node 0 - connected to 2)
#   [0, 0, 1, 1], (node 1 - connected to 2, 3)
#   [1, 1, 0, 1], (node 2 - connected to 0, 1, 3)
#   [0, 1, 1, 0]  (node 3 - connected to 1, 2)
# ]

# undirected
class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    def add_vertex(self, node):
        self.number_of_nodes += 1
        self.adjacency_list[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.adjacency_list and node2 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
            return True
        return False

    def show_connections(self):
        if self.adjacency_list:
            for key, value in self.adjacency_list.items():
                if key and value:
                    print(f"{key} -> {value}")
                else:
                    print(f"{key} -> []")


graph = Graph()
vertices = ['0', '1', '2', '3', '4', '5', '6']
for vertex in vertices:
    graph.add_vertex(vertex)

graph.add_edge('3', '1')
graph.add_edge('3', '4')
graph.add_edge('4', '2')
graph.add_edge('4', '5')
graph.add_edge('1', '2')
graph.add_edge('1', '0')
graph.add_edge('0', '2')
graph.add_edge('6', '5')

print(graph.adjacency_list)
graph.show_connections()


