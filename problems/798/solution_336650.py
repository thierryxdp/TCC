def freq_palavras(frases):
    palavras={}
    for palavra in frase:
        if palavra in palavras:
            palavras[palavra]+=1
        else:
            palavras[palavra]=1
    return palavras