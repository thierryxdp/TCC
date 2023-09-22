def eh_quadrada(matriz):
    """Função que identifica se uma matriz é quadrada ou não, retornando True se for quadrada e False se não for.
    list -> bool """
    
    if matriz != []:
        linhas = len(matriz)
        colunas = len(matriz[0])

    if linhas != colunas:
        return False
    
    elif matriz == []:
        return True
    
    else:
        return True