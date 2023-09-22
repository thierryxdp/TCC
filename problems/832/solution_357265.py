def eh_quadrada(matriz):
    if matriz ==[]:
        return True
    
    
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha != coluna:
        return False
   
    return True