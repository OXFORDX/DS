import numpy as np
import json


class Graph:

    def __init__(self, graph):
        if type(graph) is dict:
            self.array = np.array(np.copy(self.create_matrix(graph)), dtype=int)
        elif type(graph) is str:
            self.array = np.array(np.copy(self.load(graph)), dtype=int)
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


g = Graph('j_graph.json')
g.dfs(0)
g.bfs(0)
