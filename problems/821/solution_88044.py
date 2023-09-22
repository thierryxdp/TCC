def fatorial (num):
    """função que dada um número, calcula o fatorial
    dele"""
    ""'int -> int"""
    i = 1
    n_fat = 1

    while i <= num:
        n_fat = n_fat * i
        i = i + 1
    return n_fat