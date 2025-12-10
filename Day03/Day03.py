with open("Day3/f.txt", "r") as f:
    x = f.read().strip()
    
x = x.split('\n')

def lv(line, depth):
    if depth == 0:
        return ''
    if depth == 1:
        return max(line)
    num1 = max(line[:-depth+1])
    loc = line.index(num1)
    return num1 + lv(line[loc+1:], depth-1)

total = 0
for line in x:
    num1 = max(line[:-1])
    loc = line.index(num1)
    num2 = max(line[loc+1:])
    total += int(num1 + num2)
    
print(total)

total2 = 0
for line in x:
    total2 += int(lv(line, 12))
    
print(total2)