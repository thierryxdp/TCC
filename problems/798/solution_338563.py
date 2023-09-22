def freq_palavras(f):
    d = {}
    l = f.strip()
    for i in l:
        d = {i: (list.count(l, i))}
        return l