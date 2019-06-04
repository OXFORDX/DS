import numpy as np
import json


class Graph:

    def __init__(self, graph):
        if type(graph) is dict:
            self.array = np.copy(self.create_matrix(graph))
        elif type(graph) is str:
            self.array = np.copy(self.load(graph))
        else:
            self.array = np.copy(graph)

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
            json.dump(self.G, file, indent=1)
