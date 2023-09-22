def eh_quadrada (matriz):
    """ A função eh_quadrada identifica se uma matriz é quadrada ou nao. Observação: uma matriz vazia (sem nenhuma linha nem coluna) é considerada quadrada
    list --> bool
    """
    if len(matriz) == 0:
        return True
    else:
        return len(matriz) == len(matriz[0])