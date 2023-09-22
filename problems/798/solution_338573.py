def freq_palavras(f):
    v = 1
    d = {}
    l = str.split(f)
    for i in l:
        d = {i: (list.count(l, i))}
        v += i
        return v