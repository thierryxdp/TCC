def freq_palavras(frases):
    d = dict()
    for palavra in frases.split():
        if palavra not in d:
            d[palavra] = 1
        else:
            d[palavra] += 1
    return d