import json
import numpy as np
import random


class lab8:
    def __init__(self):
        self.G = {}
        self.inf = 99999
        self.arr = []
        self.matr = []
        self.visited = []

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
        self.visited = [False] * len(self.matr)
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

    def _add_edge(self, a, b, weight):
        if a == b:
            return 'The same'
        weight = int(weight)
        if a not in self.G:
            self.G[a] = {b: weight}
        else:
            self.G[a][b] = weight

    def randomgen(self, v):
        somelen = v
        helparr = np.zeros([somelen, somelen], dtype=int)
        print('Creating graph...')
        for i in range(v):
            for j in range(v):
                k = random.randrange(0, v * 2)
                x = random.randrange(0, 2)
                if x == 1 and i != j:
                    if helparr[i][j] != 1:
                        self.add_edge(str(i), str(j), k)
                        helparr[i][j] = 1
                else:
                    continue
        print('Graph created')
        print(self.G)
        self.create_matrix()
        print(self.matr)
        print(self.G)
