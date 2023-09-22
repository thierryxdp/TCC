def freq_palavras(f):
    r = []
    l = str.split(f)
    for i in l:
        r.append((i, list.count(l, i)))
    r = dict(r)
    return r