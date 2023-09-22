def freq_palavras(frases):
    ''' '''
    palavras=frases.split()
    dicionario={}
    #i=0
    for i in palavras:
        dicionario[i]=palavras.count(i)
        #i+=1
    return dicionario