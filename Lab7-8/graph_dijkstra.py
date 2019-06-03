import json
import time
import random
import numpy as np


class graph:
    def __init__(self):
        self.G = {}
        self.inf = 99999
        self.arr = []
        self.matr = []

    def __repr__(self):
        st = ''
        if len(self.G) != 0:
            for i, j in self.G.items():
                st += str(i) + str(j) + '\n'
            return st

        else:
            return 'Graph is empty'

    def create_matrix(self):
        x = len(self.G)
        self.matr = np.zeros([x, x], dtype=int)
        for i, j in self.G.items():
            for x, y in j.items():
                self.matr[int(i), int(x)] = y
        return self.matr

    def load(self, files):
        try:
            print('Try to open json...')
            with open(files, 'r') as file:
                print('File opened successfully!')
                x = json.load(file)
                self.G = x
                print(self.create_matrix())
        except FileNotFoundError:
            print('File not found!')

        finally:
            self.create_matrix()
            return self.G

    def save(self, files):
        with open(files, 'w') as file:
            json.dump(self.G, file, indent=1)

    def add_edge(self, a, b, weight):
        self._add_edge(a, b, weight)
        self._add_edge(b, a, weight)

    def _add_edge(self, a, b, weight):
        if a == b:
            return 'The same'
        weight = int(weight)
        if a not in self.G:
            self.G[a] = {b: weight}
        else:
            self.G[a][b] = weight

    def djkstra(self, start, finish):
        print('ok')
        start = str(start)
        finish = str(finish)
        Q = []
        s = {}
        s[start] = 0
        Q.insert(0, start)
        while Q:
            print(Q)
            v = Q.pop()
            for u in self.G[v]:
                if u not in s or (s[v] + self.G[v][u]) < s[u]:
                    s[u] = s[v] + self.G[v][u]
                    if u not in Q:
                        Q.insert(0, u)

        return str(start) + ' -> ' + str(finish) + ': ' + str(s[finish])

    def floyd_warshall(self, start, stop):
        A = self.matr
        n = len(A)
        for i in range(n):
            for j in range(n):
                if A[i][j] == 0:
                    A[i][j] = self.inf
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if A[i][k] < self.inf and A[k][j] < self.inf and A[i][k] + A[k][j] < A[i][j]:
                        A[i][j] = A[i][k] + A[k][j]
        for i in range(len(A)):
            A[i][i] = 0
        return str(start) + ' -> ' + str(stop) + ': ' + str(A[start][stop])

    def dfs(self, v):
        self.create_matrix()
        print('v' + str(v), end=' ')
        self.visited[v] = True
        for w in self.ways[v]:
            if w != 100000 and self.visited[w] is False:
                self.dfs(w)

    def bfs(self, start):
        self.matrix()
        explored = []
        queue = [start]
        visited = [start]
        while queue:
            node = queue.pop(0)
            explored.append('v' + str(node))
            neighbours = []
            for i in self.ways[node]:
                if i != 100000:
                    neighbours.append(i)
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
        return explored

    def BellmanFord(self, src):
        k = len(self.G)
        dist = [float("Inf")] * k
        dist[src] = 0
        for i in range(k - 1):
            for u, v, w in self.G:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.G:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        self.printArr(dist)

    def randomgen(self, v):
        somelen = v
        helparr = np.zeros([somelen, somelen], dtype=int)
        print('Creating graph...')
        for i in range(v):
            for j in range(v):
                k = random.randrange(0, v * 2)
                x = random.randrange(0, 100)
                if x == 1 and i != j:
                    if helparr[i][j] != 1 and helparr[j][i] != 1:
                        self.add_edge(str(i), str(j), k)
                        helparr[i][j], helparr[j][i] = 1, 1
                else:
                    continue
        print('Graph created')
        self.create_matrix()
        print(self.matr)
        print(self.G)

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                    # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    def FordFulkerson(self, source, sink):

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

        return max_flow


g = graph()
g.load('j_graph.json')
print(g.djkstra(0, 16))
print(g.floyd_warshall(0, 16))
g.bfs(0)
g.d
g.BellmanFord(0)
