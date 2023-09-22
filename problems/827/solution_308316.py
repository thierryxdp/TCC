def qtd_divisores(n):
    """"""
    expoente2 = 0
    if n < 0:
        return 0
    else:
    while n % 2 == 0:
        expoente2 = expoente2 + 1
    return expoente2