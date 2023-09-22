def soma_h(x):
    """A função soma 1/n que é definido por x """
    r = 1
    for i in range(2, x+1):
        if x>0:
            r = r + 1/i
    return round(r, 2)