def fatorial(n):
    """Função que calcula o fatorial do número n dado;
    int -> int."""
    mult = 1
    while mult < (n - 1):
        mult = mult + 1
        fatn = n * mult
    return fatn