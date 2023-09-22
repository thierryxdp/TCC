def eh_quadrada(matriz):
    """recebe uma matriz e retorna True se ela for quadrada, e False caso nao
    seja
    list -> bool"""
    
    nlinha = len(matriz)
    
    if nlinha == 0:
        return True
    
    else:
        
        ncoluna = len(matriz[0])
        
        if nlinha == ncoluna:
            return True
        
        else:
            return False