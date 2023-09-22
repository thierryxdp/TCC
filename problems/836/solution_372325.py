def busca(c,matriz):
    z=[]
    h=len(matriz)
    for i in range(h):
        for j in range(h):
            if matriz[i][2]==c:
                list.remove(matriz[i],matriz[i][2])
                z.append(matriz[i])
    return z