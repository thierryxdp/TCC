def fatorial(N):
    """Tem como objetivo calcular o fatorial de um 
    número.
    int > int"""
    fatorial = 1
    for n in range(1, N + 1, 1):
        fatorial *= n
    return fatorial