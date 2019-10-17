import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class CompleteGraph {

    private Map<String, Integer[]> graph;

    public CompleteGraph() {
        this.graph = new HashMap<String, Integer[]>();
    }

    // Adds a node to the graph
    public void addNode(String name, Integer x, Integer y) {
        Integer[] coordinates = new Integer[2];
        coordinates[0] = x;
        coordinates[1] = y;
        this.graph.put(name, coordinates);
    }

    // Returns an ArrayList of all the nodes in the Complete Graph
    public ArrayList<String> getNodes() {
        ArrayList<String> nodes = new ArrayList<String>();
        for (Map.Entry<String, Integer[]> entry : graph.entrySet()) {
            nodes.add(entry.getKey());
        }

        return nodes;
    }

    // Prints the nodes and the corresponding coordinates
    public void displayGraph() {
        for (Map.Entry<String, Integer[]> entry : graph.entrySet()) {
            System.out.println("Node = " + entry.getKey() + "\t" + "Coordinates = " + "(" + entry.getValue()[0] + ", "
                    + entry.getValue()[1] + ")");
        }
    }

    public int getNumberOfRoutes() {
        int length = this.getNodes().size();
        int result = 1;
        for (int i = 1; i <= length; i++) {
            result = result * i;
        }

        return result;
    }

    public Map getGraph() {
        return this.graph;
    }

}
