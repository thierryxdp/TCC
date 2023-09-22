def fatorial(n):
    '''funcao que calcula o fatorial de  um numero;
    int -> int'''
    i = 1
    fatorial = 1
    while i <= n:
        fatorial = fatorial * i
        i = i + 1
    return fatorial