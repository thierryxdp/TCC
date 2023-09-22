def fatorial(n):
    """Dado um número n, a função retorna o fatorial desse número;
    int->int"""
    fatorial=0
    multiplicador=n-1
    while 1>multiplicador:
        fatorial=fatorial+n*multiplicador
        multiplicador=multiplicador-1
    return fatorial