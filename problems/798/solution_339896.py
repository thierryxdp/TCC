def freq_palavras(frases):
    palavras = str.split(frases)
    aparicoes = {}
    
    for palavra in palavras:
        if palavra in aparicoes:
            aparicoes[palavra] +=1
        else:
            aparicoes[palavra] = 1
        return aparicoes