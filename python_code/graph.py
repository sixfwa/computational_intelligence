import math
import operator
from random import shuffle
from utils import from_csv
from algorithms import random_search

# This graph assumes that all the nodes added are all connected
# to each other.


class CompleteGraph:

    def __init__(self):
        self.graph = {}

    def add_node(self, name, coordinates):
        self.graph[name] = coordinates

    def get_node(self, name):
        return self.graph[name]

    # Returns a list of all the nodes on the complete graph
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

    def number_of_tours(self):
        number_of_nodes = len(self.get_nodes())
        return math.factorial(number_of_nodes - 1)

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
    def get_tour_cost(self, nodes):
        num_nodes = len(nodes)
        cost = 0
        for i in range(num_nodes):
            if i != (num_nodes - 1):
                cost += self.euclidean_distance(nodes[i], nodes[i + 1])
        return cost

    # Generates a random path. Returns a list
    def random_tour(self):
        nodes = self.get_nodes()
        shuffle(nodes)
        nodes = tuple(nodes)
        return nodes
