def qtd_divisores(n):
    """Retorna a quantidade de divisores que um numero n tem
    int -> int"""
    i = 0
    if n <= 0:
        return 0
    for s in range(1,n):
        if n%s == 0:
            i = i + 1
    return i + 1