def soma_h(n):
    s = 0
    i = 1
    while i <= n:
        s += 1/i
        i += 1
    return round(s, 2)