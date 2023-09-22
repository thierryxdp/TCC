def eh_quadrada(matriz):
    """Função que retorna um dado booleano caso a matriz dada como entrada seja quadrada
list -> bool"""

    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False