def freq_palavras(frases):
    ''' '''
    palavras=frases.split()
    dicionario={}
    i=0
    for i in palavras:
        palavras[i]=palavras.count(palavras[i])
        i+=1
    return dicionario