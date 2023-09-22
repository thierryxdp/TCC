def freq_palavras(frases):
    d = dict()
    for c in frases:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d