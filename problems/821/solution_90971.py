def fatorial(n):
    '''função que retorna o fatorial de um numero n dado como valor de entrada
    int->int'''
    proximo=n
    fatorial=n
    while 1 < proximo:
        fatorial= fatorial*(proximo-1)
        proximo = proximo -1    
    return fatorial