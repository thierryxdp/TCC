def freq_palavras(f):
    r = []
    l = str.split(f)
    for i in l:
        r.append((l, list.count(l, i)))
        return r