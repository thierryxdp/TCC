def eh_quadrada(matriz: list)-> bool:
    """Função que dada uma matriz, retorna 'True' caso a matriz seja quadrada ou
    retorna 'False', caso contrário."""
    
    if (len(matriz) == 0):
        return True
    if (len(matriz) == len(matriz[0])):
        return True
    elif (len(matriz) != len(matriz[0])):
        return False