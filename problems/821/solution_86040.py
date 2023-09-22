def fatorial(n):
    """Dado um número n, a função retorna o fatorial desse número;
    int->int"""]
    multiplicando=n
    multiplicador=n-1
    while 1<multiplicador:
        fatorial=multiplicando*multiplicador
        multiplicador=multiplicador-1
        multiplicando=fatorial
    return fatorial