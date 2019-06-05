import numpy as np
import json


class Graph:

    def __init__(self, graph):
        if type(graph) is dict:
            self.array = np.array(np.copy(self.create_matrix(graph)), dtype=int)
        elif graph in 'random':
            x = int(input('Size:'))
            self.randomizer(x)
        elif type(graph) is str and graph not in 'random':
            self.array = np.array(np.copy(self.load(graph)), dtype=int)
        elif graph is None:
            self.array = []
        else:
            self.array = np.array(np.copy(graph), dtype=int)

    def create_matrix(self, dictionary):
        x = len(dictionary)
        array = np.zeros([x, x])
        for i, j in dictionary.items():
            for x, y in j.items():
                array[int(i), int(x)] = y
        return array

    def load(self, files):
        try:
            print('Try to open json...')
            with open(files, 'r') as file:
                print('File opened successfully!')
                x = json.load(file)
            return self.create_matrix(x)
        except FileNotFoundError:
            print('File not found!')
            self.load(files)

    def save(self, files):
        with open(files, 'w') as file:
            json.dump(self.array, file, indent=1)

    def dfs(self, v):
        visited = [False] * (len(self.array))
        self._dfs(v, visited)
        print('\n')

    def _dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in self.array[v]:
            if not visited[i]:
                self._dfs(i, visited)

    def bfs(self, s):
        visited = [False] * (len(self.array))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.array[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print('\n')

    def minDistance(self, dist, sptSet):
        min_index = 0
        inf = 999999
        k = len(self.array)
        for v in range(k):
            if dist[v] < inf and not sptSet[v]:
                inf = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        inf = 99999
        k = len(self.array)
        dist = [inf] * k
        dist[src] = 0
        sptSet = [False] * k

        for cout in range(k):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(k):
                print(u, v)
                print(dist)
                print(sptSet)
                if self.array[u][v] and not sptSet[v] and \
                        dist[v] > dist[u] + self.array[u][v]:
                    dist[v] = dist[u] + self.array[u][v]
        return dist

    def floydWarshall(self):
        dist = self._floydWarshall(np.copy(self.array))
        v = len(self.array)
        for k in range(v):
            for i in range(v):
                for j in range(v):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        for i in range(v):
            dist[i][i] = 0
        return dist

    def _floydWarshall(self, dist):
        inf = 999999
        for i in range(len(dist)):
            for j in range(len(dist)):
                if not dist[i][j]:
                    dist[i][j] = inf
        return dist

    def BellmanFord(self, src):
        k = len(self.array)
        inf = 999999
        dist = [inf] * k
        dist[src] = 0
        for i in range(k - 1):
            for u, v, w in self._BellmanFord(k):
                if dist[u] != inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        return dist

    def _BellmanFord(self, k):
        graph = []
        for i in range(k):
            for j in range(k):
                if self.array[i][j]:
                    graph.append([i, j, self.array[i][j]])
        return graph

    def randomizer(self, v):
        self.array = np.random.randint(v, size=(v, v))
        print(self.array)


g = Graph('j_graph.json')
g.dfs(0)
g.bfs(0)
print(g.dijkstra(0), '\n')
print(g.floydWarshall(), '\n')
print(g.BellmanFord(0), '\n')
