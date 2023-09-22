def freq_palavras(frases):
    palavras=frases.split()
    d={}
    for el in palavras:
        d[el]=palavras.count(el)
    return d