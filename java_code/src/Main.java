import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {

        CompleteGraph graph = CompleteGraph.createRandomGraph();
        CompleteGraph graph1 = new CompleteGraph();
        graph1.addNode("A", 12,35);
        graph1.addNode("B", 23,25);
        graph1.addNode("C", 21,17);
        graph1.addNode("D", 45,45);
        graph1.addNode("E", 35,12);
        graph1.addNode("F", 10,34);

        Algorithm search = new Algorithm();
        System.out.println(search.twoOptNeighbourHood(graph1.generateTourPath()));


    }

}
