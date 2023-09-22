def freq_palavras(frases):
    ''' '''
    frases.split()
    dicionario={}
    i=0
    for i in frases:
        dicionario[frases[i]]=frases.count(frases[i])
        dicionario+=1
        i+=1
    return dicionario