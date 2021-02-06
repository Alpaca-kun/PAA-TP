#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define INF 1000000000

int main() {
    int V, E, u, v, w;
    // vector<vii> adjList;
    vector<vii> adjList(V, vii());
    // Initial index is 1 and final index is N

    cin >> V >> E;
    for (int i = 0; i < E; i++) {
        cin >> u >> v >> w;
        // u -= 1; v -= 1; // Adjust to initialize in index zero
        adjList[u].push_back(ii(v, w));

        cout << "a" << endl;
    }

    vi distance(V, INF);
    distance[0] = 0;

    priority_queue<ii, vector<ii>, greater<ii>> pq;
    pq.push(ii (0, 0));

    while (!pq.empty()) {
        ii front = pq.top(); pq.pop();
        int d = front.first, u = front.second;

        if (d > distance[u]) continue;
        for (int j = 0; (int)adjList[u].size(); j++)  {
            ii v = adjList[u][j];
        
            if (distance[u] + v.second < distance[v.first]) {
                distance[v.first] = distance[u] + v.second;
                pq.push(ii (distance[v.first], v.first));
            }
        }
    }

    for (int i = 0; i < V; i++) // index + 1 for final answer
        printf("SSSP(%d, %d) = %d\n", 0, i, distance[i]);

    return 0;
}