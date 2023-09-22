def freq_palavras (frases):
    d = ()
    for x in frases:
        if x in d:
            return frases.count(x)