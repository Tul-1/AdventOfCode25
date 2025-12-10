import math
from tqdm import tqdm
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from timer import Timer
import networkx as nx
import collections
from functools import lru_cache

with Timer('program'):
    with open("Day7/f.txt", "r") as f:
        x = f.read().strip()

    x = [list(i) for i in x.split('\n')]
    connections = {}

    G = nx.DiGraph()

    # . = 0
    # ^ = 1
    # S = 2

    with Timer('add nodes'):
        for row, rowItem in enumerate(x):
            for col, item in enumerate(rowItem):
                if item == '^':
                    G.add_node((col, row, 1))
                if item == 'S':
                    G.add_node((col, row, 2))

    with Timer('sort nodes'):
        sortedNodes = list(G.nodes())
        sortedNodes.sort(key=lambda x: x[1])

    with Timer('add edges'):
        for node in sortedNodes:
            l = False
            r = False
            for node2 in sortedNodes:
                if l and r:
                    break
                if node2[1] <= node[1]:
                    continue
                if node == node2:
                    continue
                
                if node[0] == node2[0] and node[2] == 2:
                    G.add_edge(node, node2)
                    break
                elif node2[0] - node[0] == 1 and node[2] == 1:  # right
                    if r:
                        continue
                    G.add_edge(node, node2)
                    r = True
                elif node2[0] - node[0] == -1 and node[2] == 1:  # left
                    if l:
                        continue
                    G.add_edge(node, node2)
                    l = True

    with Timer('calc no of splits'):
        START = (70, 0, 2)
        successors = nx.dfs_successors(G, source=START)
        x = collections.deque()
        x.append(START)
        total = 0
        while len(x) > 0:
            node = x.popleft()

            if node in successors:
                for node2 in successors[node]:
                    x.append(node2)
                    total += 1

        print(total)

    @lru_cache
    def get_timelines(node):
        if len(list(G.successors(node))) == 0:
            return 2
        if len(list(G.successors(node))) == 1 and node[2] == 1:
            return get_timelines(list(G.successors(node))[0]) + 1
        else:
            total = 0
            for node2 in G.successors(node):
                total += get_timelines(node2)
            return total

    with Timer('get no of timelines'):
        print(get_timelines(START))
    # for node in sortedNodes:
    #     print(node, get_timelines(node), (list(G.successors(node))))
    # print(x)
    # a = list(x)
    # a.sort(key=lambda x: x[1])
    # print(a)