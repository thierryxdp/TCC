def eh_quadrada(matriz):
    lista=[]
    f=len(matriz)
    k=len(matriz[0])
    if k==f:
        return True
    elif k==0 or f==0:
        return True
    else:
        return False