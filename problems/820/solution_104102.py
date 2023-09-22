def posLetra (s, l, n):
    j = str.replace (s, '-', n)
    v = str.index (j, '-', -1, 0)
    return v