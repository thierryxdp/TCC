def fatorial(numero):
    '''retorna o fatorial de n
    int -> int'''
    n = numero
    i = 1
    f = 1  
    while i <= n:
        f = f * i 
        i = i + 1
    return n, f