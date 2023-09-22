def freq_palavras(frases):
    dicio = {}
    n = 0
    frasedit = str.split(frases,' ')
    for palavra in frasedit:
        if palavra in frasedit:
        	dicio[palavra] = n+1
    return dicio