def freq_palavras (frases):
    for x in frases:
        if x in frases:
            return frases.count (x,frases[0], frases [-1])