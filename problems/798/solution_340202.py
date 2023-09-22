def freq_palavras(frases):
    frase = str.split(frases,' ')
    freq = {}
    for e in frase:
        freq[e] = list.count(frase,e)
	return freq