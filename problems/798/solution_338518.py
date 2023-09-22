def freq_palavras(frases):
    D = {}
    L = str.split(frases)
    for p in L:
        D.update({p: list.count(L, p)})
    return D