def eh_quadrada(matriz):
    f=len(matriz)
    if f==0:
        return True
    k=len(matriz[0])
    if k==f:
        return True
    else:
        return False