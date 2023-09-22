def eh_quadrada (matriz: list)->bool:
    """Função que identifica se uma matriz é quadrada e retorna True caso seja, e False caso não seja quadrada."""
    if len(matriz) == len(matriz[0]) or len(matriz) == 0 :
        return True
    else:
        return False