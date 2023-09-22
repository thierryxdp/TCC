def freq_palavras(frases):
    ''' '''
    palavras=frases.split()
    dicionario={}
    i=0
    for i in palavras:
        frase1=palavras.count(palavras[i])
        dicionario+=frase1
        i+=1
    return dicionario