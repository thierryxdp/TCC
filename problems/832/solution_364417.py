def eh_quadrada(matriz):
    if matriz == []:
        return True
    linha = len(matriz)
    col = len(matriz[0])
    if linha == col:
         return True
    if matriz == '[]':
        linha = 0
        col = 0
        return True 
    else :
        return False