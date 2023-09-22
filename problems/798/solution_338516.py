def freq_palavras(frases):
    L = str.split(frases)
    for p in L:
        D = D.update({p: list.count(L, p)})
    return D