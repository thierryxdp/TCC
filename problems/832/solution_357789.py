def eh_quadrada(matriz):
    """Função que identifica se uma matriz é quadrada ou não, retornando True se for quadrada e False se não for.
    list -> bool """

    if matriz == []:
        linhas = 0
        colunas = 0

    else:
        linhas = len(matriz)
        colunas = len(matriz[0])



    if linhas != colunas:
        return False
    
    else:
        return True