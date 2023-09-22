def qtd_divisores(n):
    """
    """
    ls = []
    for e in range(len(n)):
        if n % e == 0:
            ls.append(e)
    return len(ls)