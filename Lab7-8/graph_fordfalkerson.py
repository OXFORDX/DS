
class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])

    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns the min-cut of the given graph
    def minCut(self, source, sink):
        source -= 1
        sink -= 1
        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            # print the edges which initially had weights
        # but now have 0 weight
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == 0 and self.org_graph[i][j] > 0:
                    print(str(i) + " - " + str(j))
        print(self.graph)

    def para(self):
        n = len(self.graph)
        visit = [False] * n
        for i in range(n):
            for j in range(n):
                if graph[i][j]:
                    print(i, j)
                    print(graph[i][j])


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

g.minCut(source, sink)
