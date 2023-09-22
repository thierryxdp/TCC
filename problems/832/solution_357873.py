def eh_quadrada(matriz):
    
    
    colunas = len(matriz)
    for linhas in matriz :
        if len(linhas) != colunas :
            return False
    
    return True