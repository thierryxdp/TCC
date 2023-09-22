def eh_quadrada(matriz):
    nula=[]
    if matriz==nula:
        return True
    lin=len(matriz)
    col=len(matriz[0])
     if lin==col:
        return True
    else:
        return False