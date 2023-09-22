def melhor_volta(matriz):
    x = []
    y = []
    for j in range(6):       
        for i in range(10):
            if matriz[j][i] == min(matriz[j]):
               x.append(i)

    for s in range(6):
        y.append(matriz[s][x[s]])
    v = y.index(min(x))
    t = min(y)
    p = matriz[j].index(i) + 1
    tupla = (v + 1, t, p)
    return tupla