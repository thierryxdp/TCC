def fatorial(n):
    ''' recebe um numero e retorna seu fatorial.
    int--> int'''
    fatorial = 1
    i = 2
    while i <= n:
        fatorial = fatorial*i
        i = i +1
    return fatorial