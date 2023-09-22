def freq_palavras(a):
    d = {}
    b = a.split()
    for e in b:
        d[e] = dict.get(e, 0) + 1
    return d