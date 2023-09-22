def freq_palavras(frases):
    A = []
    B = A + [frases]
    return B
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in frases:
            D[x] = 1