with open("Day4/f.txt", "r") as f:
    x = f.read().strip()
    
# x = '''..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.'''
    
grid = [list(i) for i in x.split('\n')]

total = 0
d = [-1, 0, 1]

while True:
    oldtotal = total
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item != '@':
                continue
            c = 0
            
            for directionx in d:
                for directiony in d:
                    if directionx == 0 and directiony == 0:
                        continue
                    
                    posx = j+directionx
                    posy = i+directiony
                    if posx < 0 or posx >= len(row) or posy < 0 or posy >= len(grid):
                        continue
                    
                    if grid[posy][posx] == '@':
                        c += 1
                        
            if c < 4:
                total += 1
                grid[i][j] = '.'
                
    if total == oldtotal:
        break
                    
print(total)