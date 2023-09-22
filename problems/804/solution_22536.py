def filtra_pares(x):
    """Função que recebe uma tupla com quatro números inteiros, e devolve
    uma outra tupla contendo apenas os números pares
    tuple -> tuple"""
    t = (50, 72, 13, 6)
    li = []
    for x in t:
        if x % 2 == 0:
            li.append(x**2)
    return (li)