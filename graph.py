import math
from random import shuffle


# This graph assumes that all the nodes added are all connected
# to each other.
class CompleteGraph:

    def __init__(self):
        self.graph = {}

    def add_node(self, name, coordinates):
        self.graph[name] = coordinates

    def get_node(self, name):
        return self.graph[name]

    def get_nodes(self):
        nodes = [node for node in self.graph]
        return nodes

    def get_complete_graph(self):
        return self.graph

    def node_exists(self, node):
        if node in self.graph:
            return True
        return False

    def remove_node(self, node):
        if self.node_exists(node):
            del self.graph[node]
            return self.graph

    # Euclidean distance between two nodes. Only if those nodes
    # exist on the graph
    def euclidean_distance(self, node_1, node_2):
        if self.node_exists(node_1) and self.node_exists(node_2):
            node_1_coord = self.graph[node_1]
            node_2_coord = self.graph[node_2]
            x_dist = (node_2_coord[0] - node_1_coord[0]) ** 2
            y_dist = (node_2_coord[1] - node_1_coord[1]) ** 2
            ed = math.sqrt(x_dist + y_dist)
            return ed

    # nodes is an array
    def get_path_cost(self, nodes):
        num_nodes = len(nodes)
        cost = 0
        for i in range(num_nodes):
            if i != (num_nodes - 1):
                cost += self.euclidean_distance(nodes[i], nodes[i + 1])
        return cost

    # Generates a random path. Returns a list
    def random_path(self):
        nodes = self.get_nodes()
        shuffle(nodes)
        return nodes

    # Get the number of routes
    def get_number_of_routeS(self):
        num_nodes = len(self.get_nodes())
        

cg = CompleteGraph()
cg.add_node("A", (1, 2))
cg.add_node("B", (3, 3))
cg.add_node("C", (6, 2))
cg.add_node("D", (7, 5))
cg.add_node("E", (1, 7))
cg.add_node("F", (5, 4))
cg.add_node("G", (7, 9))
cg.add_node("H", (8, 8))
print(cg.get_complete_graph())
print(cg.euclidean_distance("A", "B"))
print(cg.random_path())
print(cg.get_path_cost(cg.random_path()))
print(cg.remove_node("B"))
print("\n")

g = CompleteGraph()
g.add_node("A", (1, 2))
g.add_node("B", (4, 5))
g.add_node("C", (3, 2))
path = g.random_path()
print("Random Route Is: {}".format(path))
print("Cost: {}".format(g.get_path_cost(path)))
