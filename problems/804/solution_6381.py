fintra_pares(x):
    """...
    """
    x = ()
    if x[0]%2 == 0:
        x = x + (x[0],)
    if x[1]%2 == 0:
        x = x + (x[1],)
    if x[2]%2 == 0:
        x = x + (x[2],)
    if x[3]%2 == 0:
        x = x + (x[3])
        return x