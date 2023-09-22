def faltante(L):
    '''
        Funcao recebe uma lista com N - 1 inteiros
        numerados de 1 a N(sem repeticoes), e retorna o
        inteiro que está faltando nesse intervalo
        list -> int
        
    '''

    i = 1
    faltante = 0
    L.sort()
    
    if L[0] != 1:
        L.insert(0,1)
        faltante = faltante + 1
        return faltante
    
    while i < len(L):
        if L[i-1] != (L[i] - 1):
            faltante = faltante + (L[i-1] + 1)
            return faltante
        i = i + 1
    
    faltante = faltante + (L[-1] + 1)
    
    return faltante