def freq_palavras(f):
    v = i
    d = {}
    l = str.split(f)
    for i in l:
        d = {i: (list.count(l, i))}
        v += d
        return v