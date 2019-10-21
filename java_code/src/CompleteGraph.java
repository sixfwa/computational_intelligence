import java.lang.reflect.Array;
import java.util.*;

public class CompleteGraph {

    private Map<String, double[]> graph;

    public CompleteGraph() {
        this.graph = new HashMap<String, double[]>();
    }

    // Adds a node to the graph
    public void addNode(String name, double x, double y) {
        double[] coordinates = new double[2];
        coordinates[0] = x;
        coordinates[1] = y;
        this.graph.put(name, coordinates);
    }

    // Returns an ArrayList of all the nodes in the Complete Graph
    public ArrayList<String> getNodes() {
        ArrayList<String> nodes = new ArrayList<String>();
        for (Map.Entry<String, double[]> entry : graph.entrySet()) {
            nodes.add(entry.getKey());
        }

        return nodes;
    }

    // Gets the coordinates of one node
    public double[] getNode(String name) {
        return graph.get(name);
    }

    // Checks whether a node exists. Returns false if it doesn't
    public boolean nodeExists(String name) {
        return this.graph.containsKey(name);
    }

    // Prints the nodes and the corresponding coordinates
    public void displayGraph() {
        for (Map.Entry<String, double[]> entry : graph.entrySet()) {
            System.out.println("Node = " + entry.getKey() + "\t" + "Coordinates = " + "(" + entry.getValue()[0] + ", "
                    + entry.getValue()[1] + ")");
        }
    }

    // Returns an int of the number of possible routes
    public long numberOfRoutes() {
        int length = this.getNodes().size();
        long result = 1;
        for (int i = 1; i <= length; i++) {
            result = result * i;
        }

        return result;
    }

    // Generate a random path
    public ArrayList<String> generateTourPath() {
        ArrayList<String> nodes = getNodes();
        Collections.shuffle(nodes);
        return nodes;
    }

    // Calculates the Euclidean Distance
    public double euclideanDistance(String nodeOne, String nodeTwo) {
        if (nodeExists(nodeOne) && nodeExists(nodeTwo)) {
            double xDistance = Math.pow((getNode(nodeTwo)[0] - getNode(nodeOne)[0]), 2);
            double yDistance = Math.pow((getNode(nodeTwo)[1] - getNode(nodeOne)[1]), 2);
            return Math.sqrt(xDistance + yDistance);
        }
        return 0;
    }

    // Calculates and then returns the cost of a route or length of a tour
    public double costOfPath(ArrayList<String> path) {
        int numberOfNodes = getNodes().size();
        double cost = 0;
        for (int i = 0; i < numberOfNodes; i++) {
            if (i != (numberOfNodes - 1)) {
                cost += euclideanDistance(path.get(i), path.get(i + 1));
            }
        }
        return cost;
    }

    public Map getGraph() {
        return this.graph;
    }

    public static CompleteGraph createRandomGraph() {
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        CompleteGraph graph = new CompleteGraph();
        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            graph.addNode(String.valueOf(alphabet[i]), random.nextInt(20) + 1, random.nextInt(20) + 1);
        }

        return graph;
    }

}
