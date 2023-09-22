def eh_quadrada(matriz):
    """Diz se a matriz inserida é quadrada ou não;
    list -> bool"""
    if len(matriz) == 0:
        return True
    
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    
    elif n_linhas == n_colunas:
        return True
    else:
        return False