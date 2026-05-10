/*
 * Adjacency List - Graph Representation
 * 
 * Uses a vector of vectors where each index represents a vertex
 * and contains a list of all vertices connected to it.
 * 
 * Time Complexity: O(V+E) for most operations
 * Space Complexity: O(V+E) - much better for sparse graphs
 * 
 * Best for: Sparse graphs, most real-world applications
 * Worst for: Dense graphs
 */

#include <iostream>
#include <vector>
using namespace std;

class Graph {
private:
    int vertices;
    vector<vector<int>> adjList;

public:
    // Constructor
    Graph(int v) {
        vertices = v;
        // Initialize adjacency list for all vertices
        adjList.resize(v);
    }

    // Add an undirected edge between two vertices
    void addEdge(int u, int v) {
        if (u >= vertices || v >= vertices || u < 0 || v < 0) {
            cout << "Invalid edge!\n";
            return;
        }
        // Add v to u's list
        adjList[u].push_back(v);
        // Add u to v's list (undirected)
        adjList[v].push_back(u);
    }

    // Add a directed edge from u to v
    void addDirectedEdge(int u, int v) {
        if (u >= vertices || v >= vertices || u < 0 || v < 0) {
            cout << "Invalid edge!\n";
            return;
        }
        // Add v to u's list only
        adjList[u].push_back(v);
    }

    // Display the adjacency list
    void display() {
        cout << "\nAdjacency List:\n";
        for (int i = 0; i < vertices; i++) {
            cout << "Vertex " << i << " -> ";
            for (int neighbor : adjList[i]) {
                cout << neighbor << " ";
            }
            cout << "\n";
        }
    }

    // Get all neighbors of a vertex
    vector<int> getNeighbors(int v) {
        if (v >= vertices || v < 0) {
            return vector<int>();
        }
        return adjList[v];
    }

    // Get degree of a vertex
    int getDegree(int v) {
        if (v >= vertices || v < 0) {
            return -1;
        }
        return adjList[v].size();
    }

    // Check if edge exists
    bool hasEdge(int u, int v) {
        if (u >= vertices || v >= vertices || u < 0 || v < 0) {
            return false;
        }
        // Check if v is in u's adjacency list
        for (int neighbor : adjList[u]) {
            if (neighbor == v) {
                return true;
            }
        }
        return false;
    }

    // Print total edges
    void printEdgeCount() {
        int edgeCount = 0;
        for (int i = 0; i < vertices; i++) {
            edgeCount += adjList[i].size();
        }
        // For undirected graphs, each edge is counted twice
        cout << "\nTotal edges: " << edgeCount / 2 << "\n";
    }
};

int main() {
    // Create a graph with 5 vertices
    Graph g(5);

    cout << "Adding edges to undirected graph...\n";
    g.addEdge(0, 1);
    g.addEdge(0, 4);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 3);
    g.addEdge(3, 4);

    g.display();

    cout << "\nNeighbors of vertex 1: ";
    vector<int> neighbors = g.getNeighbors(1);
    for (int n : neighbors) {
        cout << n << " ";
    }
    cout << "\n";

    cout << "\nDegrees of vertices:\n";
    for (int i = 0; i < 5; i++) {
        cout << "Degree of vertex " << i << ": " << g.getDegree(i) << "\n";
    }

    g.printEdgeCount();

    cout << "\nChecking edges:\n";
    cout << "Edge between 0 and 4: " << (g.hasEdge(0, 4) ? "Yes" : "No") << "\n";
    cout << "Edge between 2 and 4: " << (g.hasEdge(2, 4) ? "Yes" : "No") << "\n";

    return 0;
}
