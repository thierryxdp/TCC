def eh_quadrada(matriz: list)-> bool:
    """Função que dada uma matriz, retorna 'True' caso a matriz seja quadrada ou
    retorna 'False', caso contrário."""
    
    if (len(matriz) == 0) or (len(matriz) == len(matriz[0])):
        return True
    else:
        return False