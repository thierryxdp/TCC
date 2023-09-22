def eh_quadrada(m):
    l = len(m)
    for n in m:
        if len(n) != l:
            return False
    else:
        return True