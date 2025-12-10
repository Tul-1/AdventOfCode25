from tqdm import tqdm
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from timer import Timer

with Timer('program'):
    with Timer('import'):
        import math
        import networkx as nx

    with Timer('read'):
        with open("Day8/f.txt", "r") as f:
            x = f.read().strip()
        x = x.split('\n')
        x.sort()

    def dist3d(p1,p2):
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

    G = nx.Graph()

    with Timer('add nodes'):
        for box in x:
            G.add_node(tuple([int(i) for i in box.split(',')]))

    with Timer('find dists'):
        dists = set()
        for i, box in enumerate(list(G.nodes())[:-1]):
            for box2 in list(G.nodes())[i+1:]:
                dist = dist3d(box, box2)
                dists.add((dist, box, box2))
        dists = list(dists)
        dists.sort(key=lambda x: x[0])

    with Timer('add edges'):
        for dist, box, box2 in dists:
            spl = nx.has_path(G, box, box2)
            if spl:
                continue
            
            G.add_edge(box, box2)
            
            if len(nx.descendants(G, box)) + 1 == len(G.nodes()):
                print(box[0]*box2[0])
                exit()