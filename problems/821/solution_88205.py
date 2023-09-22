def fatorial(n):
    '''função que, dado um número retorna o fatorial desse número.
    int -> int'''
    i=1
    fator=1
    
    while i <= n:
        fator=fator*i
        i=i+1
    return fator