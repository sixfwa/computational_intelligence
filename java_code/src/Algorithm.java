import java.time.LocalTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.function.DoubleBinaryOperator;

public class Algorithm {

    /*
    A method which takes a TSP instance and a time limit in seconds. Until the time limit is reached, the method should
    generate random TSP tours, storing the best generated so far. When the time limit is reached, the best tour found
    and its length should be returned.
     */
    public HashMap<ArrayList<String>, Double> randomSearch(CompleteGraph graph, int limit) {

        LocalTime start = LocalTime.now();
        LocalTime finish = start.plusSeconds(limit);

        HashMap<ArrayList<String>, Double> optimalTour = new HashMap<>();
        ArrayList<ArrayList<String>> doneTours = new ArrayList<>();
        ArrayList<String> cheapestTour = new ArrayList<>();
        Double smallestCost = Double.MAX_VALUE;

        do {
            ArrayList<String> tour = graph.generateTourPath();
            Double cost = graph.costOfPath(tour);
            if (!doneTours.contains(tour)) {
                doneTours.add(tour);
                if (cost < smallestCost) {
                    smallestCost = cost;
                    cheapestTour = tour;
                    System.out.println("Cheapest Tour: " + cheapestTour);
                    System.out.println("Cost: " + smallestCost + "\n");
                }
            }
            start = LocalTime.now();
        } while (start.isBefore(finish));
        optimalTour.put(cheapestTour, smallestCost);

        return optimalTour;
    }

    public ArrayList<ArrayList<String>> twoOptNeighbourHood(ArrayList<String> tour) {
        ArrayList<ArrayList<String>> tours = new ArrayList<>();
        for (int i = 0; i < tour.size(); i++) {
            for (int j = 0; j < tour.size(); j++) {
                if (i != j) {
                    Collections.swap(tour, i, j);
                    if (!tours.contains(tour)) {
                        tours.add(tour);
                    }
                }
            }
        }
        return tours;
    }

}
