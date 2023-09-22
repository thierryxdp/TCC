def freq_palavras(frases):
    dicionario={}
    palavras=str.split(frases)
    for i in palavras:
        dicionario[i]=list.count(palavras,i) 
    return dicionario