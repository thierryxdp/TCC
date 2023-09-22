def eh_quadrada(matriz):
    '''Verifica se a matriz contém o msm nmr de linha e coluna.
    list -> bool
'''
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if len(matriz) == len(matriz[linha]) and len(matriz[coluna]):
                return True

            else:
                return False

    return True