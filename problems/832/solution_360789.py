def eh_quadrada(matriz):
    """Dada uma matriz (lista), a função irá verificar se
    a quantidade de linhas é igual à quantidade de colunas,
    ou seja, se é uma matriz quadrada.
    Tipo da variável matriz: list
    Tipo da saída: boolean"""
    if matriz != []:
        return len(matriz) == len(matriz[0])
    else:
        return True