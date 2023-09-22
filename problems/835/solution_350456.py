def melhor_volta(x):
    volta=(0,float('inf'),0)
    p=6
    h=10
    for i in range(p):
        for j in range(h):
            if x[i][j]<volta[1]:
                volta=(i+1,x[i][j],j+1)
    return volta