def soma_h (n):
    a = list(range(n+1))
    list.remove (a, 0)
    h = 0
    for e in a:
        h = h + (1/e)
    return round (h, 2)