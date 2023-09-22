def freq_palavras(frases):
    r = str.split(frases, " ")
    D = {}
	for x in frases:
        if x in frases:
            D[x] = list.count(r, str(x))
	return D