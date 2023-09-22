def freq_palavras(frases):
    D = {}
    L = str.split(frases)
    for p in L:
        D = D + {L[p]: L.count(p)}
    return D