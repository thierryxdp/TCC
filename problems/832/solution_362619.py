def eh_quadrada(matriz):
    """Função verifica se uma matriz é quadrada, no caso de não ter
    linhas nem colunas ela será dita como quadrada.
    list -> bool"""
    if len(matriz) == 0:
        return True
    elif len(matriz[0]) == len(matriz):
        return True
    else:
        return False