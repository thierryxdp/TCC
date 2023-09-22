def eh_quadrada(matriz):
    '''dada uma matriz, retorna se ela é quadrada ou nao
    list -> bool'''
    if len(matriz) == 0:
        return True
    else:
        lin = len(matriz)
        col = len(matriz[0])
        if lin == col:
            return True
        else:
            return False