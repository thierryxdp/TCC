def freq_palavras(f):
    d = {}
    l = list(f)
    for i in l:
        d = {i: (list.count(l, i))}
        return l