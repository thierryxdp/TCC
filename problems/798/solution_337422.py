def freq_palavras(frases):
    ''' '''
    palavras=frases.split()
    dicionario={}
    i=0
    for i in range(len(palavras)):
        dicionario[palavras[i]]=palavras.count(palavras[i])
        i+=1
    return dicionario