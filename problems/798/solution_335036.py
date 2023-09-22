def freq_palavras(frases):
    dicio = {}
    n = 1
    for palavra in frases:
        if palavra in frases:
        	dicio[palavra] = n
        	n+=1
    return dicio