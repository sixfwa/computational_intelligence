import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {

        CompleteGraph graph = new CompleteGraph();
        graph.addNode("A", 3, 4);
        graph.addNode("B", 5, 2);
        graph.addNode("C", 2, 6);
        System.out.println(graph.getNodes());
        graph.displayGraph();
        System.out.println(graph.getNumberOfRoutes());

    }

}
