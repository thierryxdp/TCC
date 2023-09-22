def soma_h(n):
    h = 0
    i = 1
    while i <= n:
        h += 1/i
        i += 1
    return round(h,2)