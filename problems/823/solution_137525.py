def faltante(L):
    '''
    
    '''
    i = 0
    j = 1
    while j <= len(L) + 1:
        contador = 0
        i = 0
        while i < len(L):
            if j == L[i]:
                contador += 1
            i += 1
        if contador == 0:
            return j
        j += 1