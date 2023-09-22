def eh_quadrada(matriz):
    '''Função que informa se a matriz é quadrada (numero de linhas igual o de
    colunas). Entrada: list(list).Saída: booleano'''
    if matriz==[]:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False