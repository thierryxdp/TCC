def freq_palavras(frases):
    ''' '''
    palavras=list(frases.split())
    dicionario={}
    i=0
    for i in palavras:
        dicionario[palavras[i]]=palavras.count(palavras[i])
        i+=1
    return dicionario