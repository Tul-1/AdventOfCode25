import math
from tqdm import tqdm
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from timer import Timer

with open("Day12/f.txt", "r") as f:
    x = f.read().strip()
    
x = x.split('\n\n')
a = x[-1]
a = a.split('\n')

total = 0
for line in a:
    s = line.split(': ')
    x,y = [int(i) for i in s[0].split('x')]
    nums = [int(i) for i in s[1].split()]
    # mx = x // 3
    # my = x // 3
    size = x * y
    if size >= sum(nums) * 9:
        total += 1
        
print(total)