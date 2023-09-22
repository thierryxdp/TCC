def eh_quadrada(matriz):
    linhas = len(matriz)
    
    if  linhas == 0:
        return True  
    colunas = len(matriz[0])
    return linhas == colunas