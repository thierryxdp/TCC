def fatorial(n):
    '''função que retorna o fatorial de um numero n dado como valor de entrada
    int->int'''
    proximo= 0
    fatorial=[]
    while 0 < proximo<n:
        fatorial = n*(proximo-1)
        proximo =proximo +1
    return fatorial