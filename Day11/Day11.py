import math
from tqdm import tqdm
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from timer import Timer

with Timer('program'):
    with Timer('import'):
        import networkx as nx
        from functools import lru_cache

    # x = '''svr: aaa bbb
    # aaa: fft
    # fft: ccc
    # bbb: tty
    # tty: ccc
    # ccc: ddd eee
    # ddd: hub
    # hub: fff
    # eee: dac
    # dac: fff
    # fff: ggg hhh
    # ggg: out
    # hhh: out'''

    with Timer('parse'):
        with open("Day11/f.txt", "r") as f:
            x = f.read().strip()
            
        x = x.split('\n')

        G = nx.DiGraph()

        for line in x:
            a = line.split(':')

            for node2 in a[1].split():
                G.add_edge(a[0], node2)

    # print(len(list(nx.all_simple_paths(G, 'you', 'out'))))


    @lru_cache
    def recur(start, end, dont):
        if start == end:
            return 1
        total = 0
        for descendant in G.successors(start):
            if descendant == dont:
                continue
            total += recur(descendant, end, dont)

        return total

    with Timer('p1'):
        print(recur('you','out',''))

    with Timer('p2'):
        a = recur('svr', 'dac', 'fft')
        b = recur('dac', 'fft', 'out')
        c = recur('fft', 'out', 'dac')

        d = recur('svr', 'fft', 'dac')
        e = recur('fft', 'dac', 'out')
        f = recur('dac', 'out', 'fft')
        print(a * b * c + d * e * f)
    # print(a, b, c, d, e, f)
