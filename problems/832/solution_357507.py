def eh_quadrada(matriz):
    """Funcao identifica se uma matriz e quadrada;
    Entrada: list
    Saida: bool"""
    if len(matriz) == len(matriz[0]):
        return True
    elif len(matriz) != len(matriz[0]):
        return False
    else:
        return True