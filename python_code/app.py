from graph import CompleteGraph
from algorithms import random_search, swap_elements, two_opt_neighbourhood
from utils import from_csv

data = from_csv("ulysses16")

graph = CompleteGraph()

# Add information from ulysses16 to the CompleteGraph
for item in data:
    name = item[0]
    coordinate = (item[1], item[2])
    graph.add_node(name, coordinate)

graph2 = CompleteGraph()
graph2.add_node("A", (3, 2))
graph2.add_node("B", (5, 8))
graph2.add_node("C", (7, 1))


tour = graph2.random_tour()
print("Original Tour: {}".format(tour))
for swap in two_opt_neighbourhood(tour):
    print(swap)
# print(tour)
# print(new_tour)

# shortest = random_search(graph, 1)
# print(shortest[1])
