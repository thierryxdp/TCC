def eh_quadrada(matriz):
    """função que retorna em valor booleano se a 
    matriz é quadrada ou não
    list=>bool"""
    if matriz==[]:
        return True
    Colunas=len(matriz[0])
    Linhas=len(matriz)
    
    if Linhas == Colunas:
        return True
    else:
        return False