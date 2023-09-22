def freq_palavras(frases):
    dicio = {}
    n = 1
    frasedit = str.split(frases,' ')
    for palavra in frasedit:
        	dicio[palavra] +=n
            n+=1
    return dicio