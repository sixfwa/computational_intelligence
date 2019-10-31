from graph import CompleteGraph
from algorithms import (best_neighbour, random_search,
                        swap_elements, two_opt_neighbourhood)
from utils import from_csv

data = from_csv("ulysses16")

graph = CompleteGraph()

# Add information from ulysses16 to the CompleteGraph
for item in data:
    name = item[0]
    coordinate = (item[1], item[2])
    graph.add_node(name, coordinate)


def testing_random_search():
    limit = 10
    print("Random Search Algorithm Example ({} seconds)".format(limit))
    shortest = random_search(graph, limit)
    print("Shortest Tour {}".format(shortest[0]))
    print("Cost: {}".format(shortest[1]))


def testing_two_opt_neighbourhood():
    tour = graph.random_tour()
    print("2-Opt Neighbourhood Example")
    print("Tour: {}".format(tour))
    for opt_tour in two_opt_neighbourhood(tour):
        print(opt_tour)


def testing_best_neighbour():
    tour = graph.random_tour()
    print("Random Tour: {}".format(tour))
    print(best_neighbour(graph, tour))


testing_best_neighbour()
# tour = graph.random_tour()
# neighborhood_tours = two_opt_neighbourhood(tour)
# costs = {}
# for neighborhood_tour in neighborhood_tours:
#     costs[neighborhood_tour] = graph.get_tour_cost(neighborhood_tour)

# for k, v in costs.items():
#     print("{} --> {}".format(k, v))
