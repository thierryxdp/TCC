def fatorial(n):
    '''retorna o fatorial de um numero n qualquer'''
    fatorial = n 
    while n > 1:
        fatorial = fatorial * (n-1)
        n = n - 1
        return fatorial