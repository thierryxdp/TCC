def freq_palavras(frases):
    frequencias = {}
    palavras = frases.split()
    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1
	return frequencias