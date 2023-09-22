def eh_quadrada(matriz):
    """Esta é a função que dada uma matriz retorna se ela é quadrada ou não, list -> bool"""

    if matriz == [[]]:
        return 

    if len(matriz) == len(matriz[0]):
        return True

    else:
        return False