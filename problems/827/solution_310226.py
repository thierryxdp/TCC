def qtd_divisores(n):
    """
    """
    ls = []
    for e in range(1, n+1):
        if n % e == 0:
            ls.append(e)
    return len(ls)