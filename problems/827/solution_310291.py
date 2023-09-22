def qtd_divisores(n):
    """ Uma função que conte quantos divisores um n° tem; int=>int"""
    v = 0
    for divisores in range(1, n + 1):
        if n % divisores == 0:
            v = v + 1
    return v