n = int(input())
tab = []
num = 2
rotation = 1
x = 0
y = 0


def step():
    global x
    global y
    global rotation
    global num
    if rotation % 4 == 1:
        if tab[y][x+1] != 0:
            rotation += 1
            num -= 1
            return 0
        tab[y][x+1] = num
        x += 1
    if rotation % 4 == 2:
        if tab[y+1][x] != 0:
            rotation += 1
            num -= 1
            return 0
        tab[y+1][x] = num
        y += 1
    if rotation % 4 == 3:
        if tab[y][x-1] != 0 or x<0 or y<0:
            rotation += 1
            num -= 1
            return 0
        tab[y][x-1] = num
        x -= 1
    if rotation % 4 == 0:
        if tab[y-1][x] != 0 or x<0 or y<0:
            rotation += 1
            num -= 1
            return 0
        tab[y-1][x] = num
        y -= 1

for i in range(n):
    tab.append([])
    for j in range(n):
        tab[i].append(0)
tab[0][0] = 1


while num <= n**2:
    try:
        step()            
    except IndexError:
        rotation += 1
        num -= 1
    num += 1


for i in range(n):
    print(tab[i])