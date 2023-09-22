def fatorial(num):
    """Recebe um número, calcula e retorna seu fatorial
    int -> int"""
    i = 1
    k = 1
    while (i <= num):
        k = k*i
        i += 1
    return k