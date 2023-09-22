def freq_palavras(frases):
    d = {x:frases.count(x) for x in set(frases)}
    return d