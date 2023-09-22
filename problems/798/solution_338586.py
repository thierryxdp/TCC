def freq_palavras(frases):
    r = dict()
    for frase in frases.split():
        if frase in r:
            r[frase] += 1
        else:
            r[frase] = 1
    return r