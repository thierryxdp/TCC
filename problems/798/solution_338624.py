def freq_palavras (frases):
    d = ()
    for x in frases:
        if x in len (d):
            return frases.count (x)