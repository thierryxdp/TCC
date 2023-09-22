def fatorial(n):
    """Função que calcula o fatorial do número n dado;
    int -> int."""
    mult = 1
    fatn = 1
    while mult <= n:
        mult = mult + 1
        fatn = (fatn * mult) / n
    return fatn