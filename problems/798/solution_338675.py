def freq_palavras(frases):
    r = str.split(frases, " ")
    D = {}
    k = 0
	for x in r:
        if x in frases:
            D[x] = k + 1
	return D