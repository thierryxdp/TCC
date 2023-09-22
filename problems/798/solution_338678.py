def freq_palavras(frases):
    A = ''
    B = A + [str.sort(frases)]
    return B
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in frases:
            D[x] = 1