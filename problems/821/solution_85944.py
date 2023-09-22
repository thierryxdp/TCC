def fatorial(n):
''' calcula o fatorial do numero n
int -> int'''
    fatorial = 1
    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    return fatorial