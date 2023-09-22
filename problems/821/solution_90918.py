def fatorial(n):
    '''
    Recebe um inteiro n e retorna um inteiro que é seu fatorial
    
    int -> int
    '''
    i=0
    fator=1
    while i<n:
        fator=fator*(i+1)
    return fator