def freq_palavras(frases):
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in r:
            D[x] = str.count(frases, x)
	return D