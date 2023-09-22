def media_matriz(matriz):
    h=[]
    for x in matriz:
        h=h+sum(matriz[x])
    p=sum(h)
    return round(p,2)