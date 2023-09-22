def fatorial(n):
    """Determinar o fatorial de um numero dado por referencia;
    int -> int"""
    acum = 1
    x = 1
    while x <= n:
        acum *= x
        x += 1
    return acum