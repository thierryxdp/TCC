def eh_quadrada(matriz):
    
    linha= len(matriz)
    coluna= len(matriz[0])
    
    if len(matriz) == 0:
        return True
    elif linha=coluna:
        return True
    else:
        return False