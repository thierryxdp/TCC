def melhor_volta(a):
    b = (0,10000,0)
    for x in range(len(a)):
        for y in range(len(a)):
            if a[x][y] < b[1]:
                b = (x+1, a[x][y], y+1)
    return b