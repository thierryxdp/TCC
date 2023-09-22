def freq_palavras(frases):
    A = []
    B = A + [frases]
    C = frases.sort()
    return B
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in frases:
            D[x] = 1