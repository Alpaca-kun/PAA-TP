from heapq import heappush, heappop

def main():
    INF = int(1e9)

    V, E = [int(x) for x in input().split()]
    adjList = [ [] for u in range(V)] # ajustar para espelhar os vertices
    for _ in range(E):
        u, v, w = [int(x) for x in input().split()]
        u -= 1
        v -= 1 # adapting to initial value zero
        adjList[u].append((v, w))
        adjList[v].append((u, w))

    distance = [INF for u in range(V)]
    distance[0] = 0 # source
    pq = []
    heappush(pq, (0, 0)) # pushing zero to the source

    while (len(pq) > 0):
        d, u = heappop(pq)
        if (d > distance[u]): continue
        for v, w in adjList[u]:
            if (distance[u] + w >= distance[v]): continue
            distance[v] = distance[u] + w
            heappush(pq, (distance[v], v))

    for u in range(V):
        print("SSSP({}, {}) = {}".format(0, u, distance[u]))

main()