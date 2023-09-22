def eh_quadrada(matriz):
    '''função que dado uma matriz retorna se ela é quadrada
    ou não. list -> boolean'''
    i = 0
    if matriz == []:
        return True
    while i < len(matriz):
        l = matriz[i]
        if len(matriz) == len(l):
            r = True
        if len(matriz) != len(l):
            r = False
        i = i + 1
    return r