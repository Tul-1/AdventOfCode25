from tqdm import tqdm

with open("Day5/f.txt", "r") as f:
    x = f.read().strip()
# x = '''3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32'''
x = x.split('\n\n')

rngs = [[int(j) for j in i.split('-')] + [True] for i in x[0].split('\n')]
ids = [int(i) for i in x[1].split('\n')]

total = 0
for id in ids:
    for rng in rngs:
        if id >= rng[0] and id <= rng[1]:
            total += 1
            break

print(total)

for i, rng in enumerate(rngs):
    if not rng[2]:
        continue
    for j, rngb in enumerate(rngs):
        if not rngb[2]:
            continue
        if i == j:
            continue
        
        if rngb[1] < rng[0]:
            continue  # no overlap
        elif rngb[0] > rng[1]:
            continue  # no
        elif rngb[0] < rng[0] and rngb[1] <= rng[1]:
            rng[2] = False
            rngb[1] = rng[1]
        elif rngb[0] <= rng[0] and rngb[1] >= rng[1]:
            rng[2] = False
        # elif rngb[0] >= rng[0] and rngb[1] <= rng[1]:
        #     rngb[2] = False
        # elif rngb[0] > rng[0] and rngb[1] > rng[1]:
        #     rng[2] = False
        #     rngb[0] = rng[0]
        #else:
        #   print(rng, rngb)

total = 0
for rng in rngs:
    if rng[2]:
        total += rng[1] - rng[0] + 1
print(total)
