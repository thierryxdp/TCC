def freq_palavras(frases):
    ''' '''
    palavras=frases.split()
    dicionario={}
    i=0
    for item in palavras:
        dicionario[item[i]]+=palavras.count[palavras[i]]
    return dicionario