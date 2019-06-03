class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    def minCut(self, source, sink):
        source -= 1
        sink -= 1
        parent = [-1] * (self.ROW)
        max_flow = 0
        path_flow = float("Inf")
        s = sink
        while (s != source):
            path_flow = min(path_flow, self.graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while (v != source):
            u = parent[v]
            self.graph[u][v] -= path_flow
            self.graph[v][u] += path_flow
            v = parent[v]
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0:
                    print(str(i + 1) + " - " + str(j + 1))
        return 'Max flow: ' + str(max_flow)


# Create a graph given in the above diagram
graph = [[0, 12, 0, 1, 0, 0, 0, 0, 0, 0],
         [12, 0, 5, 0, 7, 0, 0, 9, 0, 0],
         [0, 5, 0, 3, 0, 0, 4, 0, 0, 0],
         [1, 0, 3, 0, 0, 2, 0, 0, 0, 0],
         [0, 7, 0, 0, 0, 0, 6, 0, 7, 5],
         [0, 0, 0, 2, 0, 0, 1, 0, 0, 0],
         [0, 0, 4, 0, 6, 1, 0, 0, 0, 4],
         [0, 9, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 7, 0, 0, 1, 0, 2],
         [0, 0, 0, 0, 5, 0, 4, 0, 2, 0]]

g = Graph(graph)

source = 1
sink = 10

print(g.minCut(source, sink))
print('Para:')
print('a -> D\nb -> C\nc -> F\nd -> E\ne -> B\nf -> A')
