def eh_quadrada(matriz):
    '''Função identifica se uma dada matriz é quadrada ou não;
    list -> bool'''

    if len(matriz) == len(matriz[0]) or matriz == [[]]:
        return True
    else:
        return False