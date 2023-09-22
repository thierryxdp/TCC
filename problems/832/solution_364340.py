def eh_quadrada(matriz):
    '''
    Função que retorna se uma matriz é quadrada ou não
    list--->boolean
    '''

    l = len(matriz)
    c = len(matriz[0])
        if l==c:
            return True
        else:
            return False