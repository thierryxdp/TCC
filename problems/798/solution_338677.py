def freq_palavras(frases):
    str.sort(frases)
    return frases
    r = str.split(frases, " ")
    D = {}
	for x in r:
        if x in frases:
            D[x] = 1