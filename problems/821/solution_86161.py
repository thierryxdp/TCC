def fatorial(n):
    """
    Calcula o fatorial de um número.
    int -> int

    Parameters:
    n: Parâmetro numérico, do tipo inteiro (int).
    
    Returns:
    O fatorial de um número.
    """

    i = 1
    fatorial = 1
    
    while n != 0:
        fatorial *= n
        n -= 1

    return fatorial