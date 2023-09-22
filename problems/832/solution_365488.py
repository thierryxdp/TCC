def eh_quadrada(matriz):
    j=0
    k=0
    for i in matriz:
        j=j+1
        for e in matriz[i]:
            k=k+1
            if k==j:
                return True