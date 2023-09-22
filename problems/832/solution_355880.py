def eh_quadrada(matriz):
    """Dada uma matriz, a função retorna se essa matriz é quadrada ou
    não, caso seja quadrada a função retorna 'True', caso contrário
    retorna 'False'. Matrizes vazias são consideradas quadradas;
    list(list) -> boolean"""
    return matriz == [] or len(matriz) == len(matriz[0])