def eh_quadrada(matriz):
    '''funcao que recebe uma matriz e retorna um booleano
       True caso ela seja quadrada e False caso o contrario.
       list(list) -> bool'''
    if len(matriz)==0:
        return True
    else:
        if len(matriz)==len(matriz[0]):
            return True
        else:
            return False