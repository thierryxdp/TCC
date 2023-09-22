def freq_palavras(frases):
    dicio = {}
    n = 1
    frasedit = str.split(frases,' ')
    for palavra in frasedit:
        	dicio[palavra] +=n
            if palavra in dicio:
            	dicio[palavra] +=n
    return dicio