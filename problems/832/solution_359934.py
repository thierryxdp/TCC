def eh_quadrada(matriz):
    '''função que dado uma matriz retorna se ela é quadrada ou não. boolean ->'''
    i = 0
    if m == []:
        return True
    while i < len(m):
        l = m[i]
        if len(m) == len(l):
            r = True
        if len(m) != len(l):
            r = False
        i = i + 1
    return r