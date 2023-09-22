def eh_quadrada(matriz):
    '''identifica uma matriz quadrada list(list)->boll'''
    if len(matriz) !=0:
        nlinha = len(matriz)
        ncoluna = len(matriz[0])
        if nlinha == ncoluna:
            return True 
        else:
            return False 
    else:
        return True