def fatorial (n):
    r = 1
    fatores = list(range((n+1)))
    fatores.remove (0)
    for f in fatores:
        r = r * f
    return r