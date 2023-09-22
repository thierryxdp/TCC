def fatorial(n):
    '''Recebe um numero e retorna seu fatorial'''
    cnt=0
    resultado=1
    while cnt<n:
        resultado=(resultado*(n-cnt))
        cnt=cnt+1
    return resultado