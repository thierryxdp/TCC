def media_matriz(matriz):
    a=[]
    for l in range(len(m)):
        for c in range(len(m[0])):
            a.append(matriz[l][c])
            z=sum(a)/len(matriz[c])
    return round(z,2)