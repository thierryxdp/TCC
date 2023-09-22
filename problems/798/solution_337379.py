def freq_palavras(frases):
    ''' '''
    dicionario={}
    i=0
    for i in frases.split():
        dicionario[frases.split()[i]]=palavras.count(frases.split()[i])
    i+=1
    return dicionario