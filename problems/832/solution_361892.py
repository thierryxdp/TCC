def eh_quadrada(matriz):
    lin=len(matriz)
    col=len(matriz[0])
    nula=[]
    if matriz==nula:
        return True
    elif lin==col:
        return True
    else:
        return False