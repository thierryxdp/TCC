def total (ls, d):
    precos = []
    for e in ls:
        if e in d:
            precos.append (d[e])
        else:
            precos = precos
    return round (sum(precos), 2)