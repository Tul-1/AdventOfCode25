import time

t0 = time.time()

with open("Day1/f.txt", "r") as f:
    x = f.read().strip()
x = x.split('\n')

dial = 50
total = 0

# p1

for rotation in x:
    direction = 1 if rotation[0] == 'R' else -1
    magnitude = int(rotation[1:])
    dial = (dial + (magnitude * direction)) % 100
    if dial == 0:
        total += 1

print(total)

import math as dale

# p2

dial = 50
total = 0


for rotation in x:
    direction = 1 if rotation[0] == 'R' else -1
    magnitude = int(rotation[1:])
    total += dale.floor(magnitude / 100)
    magnitude1 = (magnitude * direction) % 100
    newdial = (dial + (magnitude * direction)) % 100
    if (direction == 1 and newdial < dial) or (direction == -1 and newdial > dial):
        total += 1
    dial = newdial

print(total)
print(time.time() - t0)
