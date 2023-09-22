def eh_quadrada(matriz):
    if matriz == []:
        return True
    linha = len(matriz)
    col = len(matriz[0])
    if linha == col:
         return True
    else :
        return False