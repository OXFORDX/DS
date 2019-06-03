import heapq
import json

global freq


class Node:
    def __init__(self, prob, symbol=None):
        self.left = None
        self.right = None
        self.symbol = symbol
        self.prob = prob

    def __lt__(self, other):
        return self.prob < other.prob

    def encode(self, encoding):
        if self.left is None and self.right is None:
            yield (self.symbol, encoding)
        else:
            for v in self.left.encode(encoding + '0'):
                yield v
            for v in self.right.encode(encoding + '1'):
                yield v


class Huffman:
    def __init__(self, initial):
        global freq
        self.initial = initial

        # Count frequencies
        def frequ(initial):
            freq = {}
            for _ in initial:
                if _ in freq:
                    freq[_] += 1
                else:
                    freq[_] = 1
            return freq

        freq = frequ(initial)
        # Construct priority queue
        pq = []
        for symbol in freq:
            pq.append(Node(freq[symbol], symbol))
        heapq.heapify(pq)

        if len(pq) == 1:
            self.root = Node(1)
            self.root.left = pq[0]
            self.encoding = {symbol: '0'}
            return

        # Huffman Encoding Algorithm
        while len(pq) > 1:
            n1 = heapq.heappop(pq)
            n2 = heapq.heappop(pq)
            n3 = Node(n1.prob + n2.prob)
            n3.left = n1
            n3.right = n2
            heapq.heappush(pq, n3)

        # Record
        self.root = pq[0]
        self.encoding = {}
        for sym, code in pq[0].encode(''):
            self.encoding[sym] = code

    def __repr__(self):
        return 'huffman:' + str(self.encoding)

    def encode(self, s):
        bits = ''
        for _ in s:
            if not _ in self.encoding:
                raise ValueError("'" + _ + "' is not encoded character")
            bits += self.encoding[_]
        return bits

    def decode(self, bits):
        node = self.root
        s = ''
        for _ in bits:
            if _ == '0':
                node = node.left
            else:
                node = node.right

            if node.symbol:
                s += node.symbol
                node = self.root

        return s


def tests(number):
    global freq
    with open('path' + str(number) + '.txt', 'r') as h, open('jsonall' + str(number) + '.json', 'w') as j:
        val = []
        lengh = 0

        for line in h:
            en = Huffman(line)
            en.encoding = dict(sorted(en.encoding.items()))
            freq = dict(sorted(freq.items()))

            val = list(en.encoding.values())
            for elem in val:
                lengh += int(len(elem))
            mid_way = round(lengh / len(val))
            max_way = len(max(val, key=len))
            all_results = {'frequrency:': freq, 'bin': en.encoding, 'way': {'mid_way': mid_way, 'max_way': max_way}}
            print(mid_way, max_way)
            print(all_results)
            json.dump(all_results, j, indent=1)


tests(3000)
