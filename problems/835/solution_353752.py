def melhor_volta(matriz):
    x = []
    y = []
    for voltas in range(6):       
        for tempo in range(10):
            if matriz[voltas][tempo] == min(matriz[voltas]):
               x.append(tempo)

    for i in range(6):
        y.append(matriz[i][x[i]])
        
    v = y.index(min(y))
    t = min(y)
    p = matriz[v].index(t) + 1
    tupla = (v + 1, t, p)
    return tupla