def freq_palavras(frases):
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in frases:
            A = str.count(frases, x)
	return A