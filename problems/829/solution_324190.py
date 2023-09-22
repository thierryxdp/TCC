def soma_H (n):
    a = list(range(n+1))
    list.remove (a, 0)
    H = 0
    for e in a:
        H = H + (1/e)
    return round (H, 2)