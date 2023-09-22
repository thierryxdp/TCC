def media+matriz(matriz):
    x=0
    k=0
    for i in matriz:
        for j in i:
            x=x+j
            k=k+1
    return round(x/j,3)