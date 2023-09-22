def fatorial(n):
    '''Funcao que calcula o fatorial de um dado
    numero n; int -> int'''
    f = 0
    i = n
    while i>0:
        i -= 1
        f += n * (n-i) 
    return f