def eh_quadrada(matriz='[[]]'):
    linha = len(matriz)
    col = len(matriz[0])
    if linha == col:
         return True
    if matriz == '[]':
        linha = 0
        col = 0
        return True 
    else: 
        return False