import time
import operator
from graph import CompleteGraph


# Parameters CompleteGraph and time limit
def random_search(graph, limit):
    number_of_tours = graph.number_of_tours()
    counter = 0
    tours = {}
    start = time.time()
    finish = start + limit
    while start < finish:
        tour = graph.random_tour()
        cost = graph.get_tour_cost(tour)
        if not tour in tours:
            print("Tour: {}\tCost: {}".format(tour, cost))
            tours[tour] = cost
            counter += 1
        start = time.time()

    shortest = min(tours.items(), key=operator.itemgetter(1))
    return shortest


# Swap two element positions in a list
def swap_elements(tour, pos_1, pos_2):
    list_tour = list(tour)
    list_tour[pos_1], list_tour[pos_2] = list_tour[pos_2], list_tour[pos_1]
    tuple_tour = tuple(list_tour)
    return tuple_tour


# Takes a tour as input and returns the 2-opt neighbourhood of
# the tour as output
def two_opt_neighbourhood(tour):
    switched_tours = []
    for i in range(len(tour)):
        for j in range(len(tour)):
            switched = swap_elements(tour, i, j)
            if not switched in switched_tours and not switched == tour and not switched[::-1] in switched_tours:
                switched_tours.append(switched)
    return switched_tours


# Best Neighbour Step Function
# Takes a neighbourhood (with the same structure as that returned by the two opt function)
# and returns the shortest tour in the neighbourhood
def best_neighbour(graph, tour):
    neighbourhood_tours = two_opt_neighbourhood(tour)
    cost_dictionary = {}
    for neighbourhood_tour in neighbourhood_tours:
        cost_dictionary[neighbourhood_tour] = graph.get_tour_cost(tour)

    shortest = min(cost_dictionary.items(), key=operator.itemgetter(1))
    return shortest
