def freq_palavras(frases):
    frase = str.split(frases)
    d = {}
    for i in frase:
        c = str.count(frases, i)
        d[i] = c
    return d