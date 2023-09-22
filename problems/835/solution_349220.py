def melhor_volta(matriz):
    
    c = range(6)
    v = range(10)
    t = (0,float('inf'),0)
    
    for i in c:
        for j in v:
            if matriz[i][j] < t[1]:
               t = (i+1, matriz[i][j], j+1)
    return t