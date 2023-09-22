def fatorial(n):
    """Função que calcula o fatorial do número n dado;
    int -> int."""
    mult = 1
    fatn = n
    while mult < n:
        mult = mult + 1
        fatn = fatn * mult
    return fatn