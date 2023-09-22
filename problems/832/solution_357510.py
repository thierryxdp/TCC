def eh_quadrada(matriz):
    """Funcao identifica se uma matriz e quadrada;
    Entrada: list
    Saida: bool"""
    vazio = []
    if len(matriz) == len(matriz[0]):
        return True
    if matriz == vazio:
        return True
    else:
        return False