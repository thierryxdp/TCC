def soma_h(n):
    h = 0
    i = 0
    while i > n:
        i = i+1
        h = h + (1/i)
    return round(h,2)