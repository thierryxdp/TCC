def media_matriz(matriz):
    total=0
    zeros=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            n_elem=len(matriz)*len(matriz[0])
        total=total+1
    return round(((n_elem)/total),2)