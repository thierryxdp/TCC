def faltante(L):
    '''
        Funcao recebe uma lista com N - 1 inteiros
        numerados de 1 a N(sem repeticoes), e retorna o
        inteiro que está faltando nesse intervalo
        list -> int
        
    '''

    i = 0
    faltante = 0
    L.sort()
    
    while i < (len(L) - 1):
        if L[i] != (L[i+1] - 1):
            faltante = faltante + (L[i] + 1)
        i = i + 1
    return faltante