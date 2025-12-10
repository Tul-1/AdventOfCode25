import math
from functools import lru_cache
from tqdm import tqdm

import networkx as nx

with open("Day8/f.txt", "r") as f:
    x = f.read().strip()
x = x.split('\n')
x.sort()

def dist3d(p1,p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

G = nx.Graph()

for box in x:
    G.add_node(tuple([int(i) for i in box.split(',')]))

dists = set()
for box in G.nodes():
    for box2 in G.nodes():
        if box == box2:
            continue
        
        dist = dist3d(box, box2)
        if (dist,box2,box) in dists:
            continue
        dists.add((dist, box, box2))
dists = list(dists)
dists.sort(key=lambda x: x[0])
dists = dists[:1000]

for dist, box, box2 in dists:
    spl = nx.has_path(G, box, box2)
    if spl:
        continue
    
    G.add_edge(box, box2)

circuits = []
visited = set()
for box in G.nodes():
    if box in visited:
        continue
    nodes = nx.descendants(G,box)
    nodes.add(box)
    circuits.append(nodes)
    for node in nodes:
        visited.add(node)
circuits.sort(key=lambda x: len(x), reverse=True)
print(len(circuits[0])*len(circuits[1])*len(circuits[2]))