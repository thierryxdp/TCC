def fatorial(n):
    '''função que calcula o fatorial de um número recebido. int -> int'''
    fatorial = 1
    while n > 0:
         fatorial = fatorial * n
         n = n - 1
    if n < 0:
        fatorial = 'indefinido'
    return fatorial