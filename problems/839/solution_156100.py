def carros(n, c):
    """."""
    if c not in carros and n%c > 0:
        return (n//5) + 1
    elif c not in carros and n%c == 0:
        return n/5
    elif c > 0 and n%c > 0:
        return (n//c) + 1
    else:
        return (n/c)