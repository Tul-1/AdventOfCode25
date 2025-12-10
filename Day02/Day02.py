with open("Day2/f.txt", "r") as f:
    x = f.read().strip()
x = x.split(',')
x = [[int(i) for i in item.split('-')] for item in x]

total = 0
c = 0
for _range in x:
    for num in range(_range[0], _range[1] + 1):
        if len(str(num)) % 2 != 0:
            continue

        l = int(len(str(num)) / 2)

        p1 = str(num)[:l]
        p2 = str(num)[l:]

        if p1 == p2:
            total += num

        c += 1
        
print(c)

print(total)
