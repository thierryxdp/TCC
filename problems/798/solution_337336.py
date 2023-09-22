def freq_palavras(frases):
    ''' '''
    palavras=frases.split()
    dicionario={}
    i=0
    for palavras[i] in palavras:
        dicionario+=palavras.count[palavras[i]]
    return dicionario