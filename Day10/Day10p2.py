import math
from tqdm import tqdm
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from timer import Timer
from z3 import *

abc = []

with Timer('program'):
    with open("Day10/f.txt", "r") as f:
        x = f.read().strip()
    x = x.split('\n')

    total = 0

    d = []
    for i, line in enumerate(tqdm(x)):
        ctx = Context()
        s = Optimize(ctx=ctx)
        new = {'lights': [], 'buttons': [], 'lights_controls': [], 'joltage': ()}
        a = line.split(' ')
        for j, ch in enumerate(a[-1][1:-1].split(',')):
            jolt_val = int(ch)
            jolt_var = Int(f'l{i}j{j}', ctx=ctx)
            constraint = jolt_var == jolt_val
            new['lights'].append(jolt_var)
            new['lights_controls'].append([])
            s.add(constraint)
            
        for k, button in enumerate(a[1:-1]):
            button_tuple = list([int(ii) for ii in button[1:-1].split(',')])
            button_val = Int(f'l{i}button{k}', ctx=ctx)
            s.add(button_val >= 0)
            
            new['buttons'].append(button_val)
            for item in button_tuple:
                new['lights_controls'][item].append(button_val)
                
        total_buttons = Int(f'l{i}total_buttons', ctx=ctx)
        constraint = total_buttons == Sum([Int(f'l{i}button{k}',ctx=ctx) for k in range(len(a[1:-1]))])
        s.add(constraint)
                            
        for j, ch in enumerate(a[0][1:-1]):
            constraint = new['lights'][j] == Sum(new['lights_controls'][j])
            s.add(constraint)
            
        s.minimize(total_buttons)
        s.check()
        m = s.model()
        # print(m)
        abc.append(m[total_buttons].as_long())
        total += m[total_buttons].as_long()
    print(total)
    print(abc)