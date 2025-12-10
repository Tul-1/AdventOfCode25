f = open("Day2/f.txt", "r")
x = f.read().strip()
#x='11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
x = x.split(',')
x = [[int(i) for i in item.split('-')] for item in x]

total = 0

for _range in x:
    for num in range(_range[0], _range[1]+1):
        l = int(len(str(num)))
        
        for section in range(1,int(l/2)+1):
            if l % section != 0:
                continue
            st = str(num)[:section]
            if str(num) == st*int(l/section):
                total += num
                break
            
print(total)