import numpy as np
import json


class Graph:
    def __init__(self, graph):
        if type(graph) is dict:
            self.array = np.array(np.copy(self.create_matrix(graph)), dtype=int)
        elif type(graph) is str and graph in 'random':
            x = int(input('Size:'))
            self.randomizer(x)
        elif type(graph) is str:
            self.array = np.array(np.copy(self.load(graph)), dtype=int)
        else:
            self.array = np.array(np.copy(graph), dtype=int)
        self.mincut_array = np.zeros([len(self.array), len(self.array)], dtype=int)

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

    def BFS(self, s, t, parent, array):
        v = len(self.array)
        visited = [False] * v
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(array[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False

    def minCut(self, source, sink):
        array = np.copy(self.array)
        org_graph = np.copy(self.array)
        k = len(self.array)
        parent = [-1] * k

        max_flow = 0
        while self.BFS(source, sink, parent, array):
            flow = 999999
            s = sink
            while s != source:
                flow = min(flow, array[parent[s]][s])
                s = parent[s]
            max_flow += flow
            v = sink
            while v != source:
                u = parent[v]
                array[u][v] -= flow
                array[v][u] += flow
                v = parent[v]
        print(array)
        print('///\nВідсічення по:')
        for i in range(k):
            for j in range(k):
                if array[i][j] == 0 and org_graph[i][j] > 0:
                    print(str(i + 1) + " - " + str(j + 1))
        print('Максимальний потік в мережі: {0}'.format(max_flow))
        return max_flow

    def cut_matrix(self):
        k = len(self.array)
        for i in range(k):
            for j in range(k):
                if i != j:
                    self.mincut_array[i][j] = self.minCut(i, j)
        return self.mincut_array

    def bpm(self, u, matchR, seen, arr):
        k = len(arr)
        graph = np.copy(arr)
        for v in range(k):
            if graph[u][v] and not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v],
                                               matchR, seen, arr):
                    matchR[v] = u
                    return True
        return False

    def _maxBPM(self, arr):
        k = len(arr)
        matchR = [-1] * k
        result = 0
        for i in range(k):
            seen = [False] * k
            if self.bpm(i, matchR, seen, arr):
                result += 1
        return 'Максимальне паросполучення в графі: \n{0}\n Дорівнює: {1}'.format(arr, result)

    def maxBPM(self):
        v = len(self.array)
        arr = np.copy(self.array)
        for i in range(v):
            for j in range(v):
                if arr[i][j]:
                    arr[i][j] = 1
        print(self._maxBPM(arr))

    def randomizer(self, v):
        self.array = np.random.randint(v, size=(v, v))


graph1 = [[0, 12, 0, 1, 0, 0, 0, 0, 0, 0],
          [12, 0, 5, 0, 7, 0, 0, 9, 0, 0],
          [0, 5, 0, 3, 0, 0, 4, 0, 0, 0],
          [1, 0, 3, 0, 0, 2, 0, 0, 0, 0],
          [0, 7, 0, 0, 0, 0, 6, 0, 7, 5],
          [0, 0, 0, 2, 0, 0, 1, 0, 0, 0],
          [0, 0, 4, 0, 6, 1, 0, 0, 0, 4],
          [0, 9, 0, 0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 7, 0, 0, 1, 0, 2],
          [0, 0, 0, 0, 5, 0, 4, 0, 2, 0]]

bpGraph = [[0, 0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 1],
           [1, 0, 0, 1, 1, 0],
           [0, 1, 0, 1, 0, 0],
           [1, 0, 0, 0, 1, 0]]
g = Graph('random')

print(g.cut_matrix())

g1 = Graph('random')
g1.maxBPM()
