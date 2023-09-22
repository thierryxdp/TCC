def freq_palavras(frases):
    frequencia = {}
    palavras = frases.split(' ')
    for i in range(0, len(palavras)):
        valor = frases.count(palavras[i])
        frequencia[palavras[i]] = valor
	
    return frequencia