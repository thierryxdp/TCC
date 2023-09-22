def fatorial(x):
    """A funcao calcula o fatorial de um numero inteiro. int-->int."""
    i = 1
    fator = 1
    while i >= x:
        fator = fator * i
        i = i + 1
    return fator