def fatorial(n):
    """Retorna o fatorial de um número n;
int -> int"""
    acumulador = 1
    
    while n != 0:
        acumulador = acumulador * n
        n = n-1
    return acumulador