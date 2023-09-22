def freq_palavras(frases):
    d = {}
    palavras = str.split(frases)
    for e in palavras:
        d[e] = list.count(S, e)
    return d