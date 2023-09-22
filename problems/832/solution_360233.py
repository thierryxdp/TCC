def eh_quadrada(matriz):
    ''' Função que dada uma matriz, retorna o valor booleano
    True se ela for quadrada e False, caso contrário.
    Entrada: list
    Retorno: bool '''

    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False