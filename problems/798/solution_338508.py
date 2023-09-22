freq_palavras(frases):
    D = {}
    L = frases.split
    for p in L:
        D = D + {L[p]: L.count(p)}
    return D