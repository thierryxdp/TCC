def freq_palavras(f):
    d = {}
    l = str.join(' ', f)
    for i in l:
        d = {i: (list.count(l, i))}
        return d