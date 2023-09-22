def eh_quadrada(matriz):
    """Verifica se uma matriz passada é quadrada ou não,
    retornando True or False.
    list[lists]->Bool"""
    for linhas in matriz:
        for colunas in range(len(linhas)):
            if len(matriz)!=len(linhas):
                return False
    return True