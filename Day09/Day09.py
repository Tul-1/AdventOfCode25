import math
from tqdm import tqdm
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from timer import Timer

with Timer('program'):
    with open("Day9/f.txt", "r") as f:
        x = f.read().strip()
    x = x.split('\n')
    x = [tuple([int(i) for i in row.split(',')]) for row in x]

    max_area = -math.inf
    a = ()
    for i, p in enumerate(tqdm(x[:-1])):
        for p2 in x[i+1:]:
            width = abs(p2[0] - p[0]) + 1
            height = abs(p2[1] - p[1]) + 1
            area = width * height
            
            if area > max_area:
                max_area = area
                a = (p,p2)
                
    print(max_area)
    print(a)