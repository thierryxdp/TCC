def freq_palavras(frases):
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in frases:
            D[x] = list(dict.values(x)) + 1
	return D