def media_matriz(matriz):
    h=[]
    for x in matriz:
        h=h+sum(matriz[x])
    p=sum(h)
    d=p/len(matriz)
    return round(p,2)