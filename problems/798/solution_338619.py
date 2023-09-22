def freq_palavras (frases):
    d = ()
    for x in frases:
        if x in d:
            d == d + frases.count(x)
    return d