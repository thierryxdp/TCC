def freq_palavras(frases):
    r = str.split(frases, " ")
    return r
    D = {}
	for x in r:
        if x in r:
            D[x] = list.count(r, x)
	return D