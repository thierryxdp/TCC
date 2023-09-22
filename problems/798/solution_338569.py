def freq_palavras(f):
    d = {}
    l = str.split(f)
    for i in l:
        d = {i: (list.count(l, i))}
        return i