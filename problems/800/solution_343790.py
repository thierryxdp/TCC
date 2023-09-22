def total (l, d):
    r = 0
    for e in l:
        r = r + round(d[e], 2)
    return r