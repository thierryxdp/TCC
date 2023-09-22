def eh_quadrada(matriz):
    ''' função booleana que indentifica se é uma matriz quadrada.
    Entrada: list;
    Saída: str'''
    if len(matriz) == 0:
        return 'True'
    if len(matriz) == len(matriz[0]):
        return 'True'
    else:
        return 'False'