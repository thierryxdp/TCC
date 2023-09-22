def freq_palavras(frases):
    dicionario={}
    palavras=str.split(frases)
    for i in palavras:
        dicionario[i]=str.count(palavras,i) 
    return dicionario