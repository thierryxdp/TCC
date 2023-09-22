def eh_quadrada(matriz):
    """
    Dada uma matriz, retorna-se True se ela for quadrada e False se nao for
    Entrada: matriz -> list(lists)
    Retorna: bool
    """
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False