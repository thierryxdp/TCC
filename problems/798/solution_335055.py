def freq_palavras(frases):
    dicio = {}
    n = 1
    frasedit = str.split(frases,' ')
    for palavra in frasedit:
        if palavra in dicio:
        	dicio[palavra] = 1+n
        else:
            dicio[palavra] = 1
    return dicio