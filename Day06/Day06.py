import math
from tqdm import tqdm
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from timer import Timer
import re

with Timer('parse'):
    with open("Day6/f.txt", "r") as f:
        x = f.read().strip()
    # x = '''123 328  51 64 
    #  45 64  387 23 
    #   6 98  215 314
    # *   +   *   +  '''
    x = x.split('\n')
    nums = [[int(i) for i in re.split(' {1,10}', line) if i] for line in x[:-1]]
    ops = [i.strip() for i in re.split(' {1,10}', x[-1].strip())]

with Timer('p1'):
    total = 0
    for x2, op in zip(range(len(nums[0])), ops):
        val = 0 if op == '+' else 1
        for y in range(len(nums)):
            if op == '+':
                val += nums[y][x2]
            else:
                val *= nums[y][x2]
        total += val
    print(total)

with Timer('p2'):
    op_iter = iter(ops[::-1])
    nums2 = [list(line) for line in x[:-1]]
    current = -1
    total = 0
    for i in range(len(nums2[0]) - 1, -1, -1):
        if current == -1:
            op = next(op_iter)

            if op == '+':
                current = 0
            else:
                current = 1

        col = [nums2[j][i] for j in range(len(nums2))]

        if col.count(' ') == len(col):
            total += current
            current = -1
        else:
            num = int(''.join(col).strip())
            # print(f'{op} {num}')
            if op == '+':
                current += num
            else:
                current *= num

        if i == 0:
            total += current

    print(total)
