def melhor_volta(x):
    volta=(0,float('inf'),0)
    for i in range(6):
        for j in range(10):
            if x[i][j]<volta:
                volta=(i+1,x[i][j],j+1)
    return volta