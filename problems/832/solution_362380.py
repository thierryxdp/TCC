def eh_quadrada(matriz):
    '''A matriz é quadrada?Eu verifico se ela contém nenhuma linha e nenhuma coluna e retorno um valor booleano.
bool -> bool'''
    for l in range(0, len(matriz)):
        for c in range(0, len(matriz[l])):
            if len(matriz) == len(matriz[l]) and len(matriz[c]):
                return True
            else:
                return False
    return True