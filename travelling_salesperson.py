import math
from random import shuffle
import pandas as pd


class Graph:

    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = {}

    def add_route(self, node_1, node_2, distance):
        if self.node_exists(node_1) and self.node_exists(node_2):
            self.graph[node_1][node_2] = distance
            self.graph[node_2][node_1] = distance
        else:
            if not self.node_exists(node_1):
                print("{} does not exist.".format(node_1))
            if not self.node_exists(node_2):
                print("{} does not exist.".format(node_2))

    # returns a list of all the nodes on the graph
    def get_nodes(self):
        nodes = []
        for node in self.graph:
            nodes.append(node)
        return nodes

    # Returns a random legal route
    def generate_random_path(self):
        nodes = self.get_nodes()
        shuffle(nodes)
        return nodes

    # returns a dictionary of all the nodes a given node is connected
    # to
    def get_routes(self, node):
        return self.graph[node]

    def node_exists(self, node):
        if node in self.graph:
            return True
        return False

    def route_exists(self, node_1, node_2):
        if node_2 in self.graph[node_1]:
            return True
        return False

    def display_graph(self):
        for node_1 in self.graph:
            print('Routes for node: {}'.format(node_1))
            for node_2 in self.graph[node_1]:
                print("{} ---> {}".format(node_1, node_2))

    # Takes an array of nodes and checks whether a path can be created with them
    # returns true if a path does exist
    def does_path_exist(self, nodes):
        n = len(nodes)
        for i in range(n):
            if i != n - 1:
                if not self.route_exists(nodes[i], nodes[i + 1]):
                    return False
        return True

    def cost_of_path(self, nodes):
        cost = 0
        n = len(nodes)
        if self.does_path_exist(nodes):
            for i in range(n):
                if i != n - 1:
                    cost += self.cost_of_route(nodes[i], nodes[i + 1])

        return cost

    # Returns the cost of going from node_1 to node_2
    def cost_of_route(self, node_1, node_2):
        if self.route_exists(node_1, node_2):
            return self.graph[node_1][node_2]

    # Only holds if the graph is fully connected. Need to make adjustments.
    def number_of_routes(self):
        n = len(self.graph)
        return math.factorial(n - 1)

    def calculate_distance(self, x_a, x_b, y_a, y_b):
        distance = math.sqrt(((x_b - x_a) ** 2) + ((y_b - y_a) ** 2))
        return distance

graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')

graph.add_route('A', 'B', 20)
graph.add_route('A', 'C', 42)
graph.add_route('A', 'D', 35)

graph.add_route('B', 'C', 30)
graph.add_route('B', 'D', 34)

graph.add_route('C', 'D', 12)

graph.display_graph()

routes = ['A', 'B', 'C', 'D']

print("Does the path exist for the path -> {}: {}".format(routes,
                                                          graph.does_path_exist(routes)))

print("Cost of path: {}".format(graph.cost_of_path(routes)))
print("Random route: {}".format(graph.generate_random_path()))

df = pd.read_csv('ulysses16.csv', index_col='id')
print(df)

input()
