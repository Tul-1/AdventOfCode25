import math
from tqdm import tqdm
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from timer import Timer
from z3 import *

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
    for j, ch in enumerate(a[0][1:-1]):
        light_val = ch == '#'
        light_var = Bool(f'l{i}ch{j}', ctx=ctx)
        constraint = light_var == light_val
        new['lights'].append(light_var)
        new['lights_controls'].append([])
        s.add(constraint)
        
    for k, button in enumerate(a[1:-1]):
        button_tuple = list([int(ii) for ii in button[1:-1].split(',')])
        button_val = Bool(f'l{i}button{k}', ctx=ctx)
        
        new['buttons'].append(button_val)
        for item in button_tuple:
            new['lights_controls'][item].append(button_val)
            
    total_buttons = Int(f'l{i}total_buttons', ctx=ctx)
    constraint = total_buttons == Sum([If(Bool(f'l{i}button{k}',ctx=ctx),1,0) for k in range(len(a[1:-1]))])
    s.add(constraint)
                        
    for j, ch in enumerate(a[0][1:-1]):
        sum = 0
        for item in new['lights_controls'][j]:
            sum += item
        constraint = (sum % 2) == new['lights'][j]
        s.add(constraint)
        
    s.minimize(total_buttons)
    s.check()
    m = s.model()
    for d in m.decls():
        if d.name() == f'l{i}total_buttons':
            total += m[d].as_long()
print(total)