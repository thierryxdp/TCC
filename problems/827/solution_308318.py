def qtd_divisores(n):
    """"""
    if n < 0:
        return 0
    else:
        expoente2 = 0
        while n > 0:
            if n % 2 == 0:
                expoente2 = expoente2 + 1
        return expoente2