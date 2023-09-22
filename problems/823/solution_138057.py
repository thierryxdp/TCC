def faltante(lista):

    '''list -> int'''
    
    falta = len(lista)+1
    N = 1
    i = 0
    while i <= falta:
        if N == falta:
            return N