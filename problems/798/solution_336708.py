def freq_palavras(frases):
    d = {}
    palavras = str.split(frases)
    for i in palavras:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d