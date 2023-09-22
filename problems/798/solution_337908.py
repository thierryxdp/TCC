def freq_palavras(frases):
    '''
    '''
    dicionario = {}
    y=str.split(frases)
    
    for x in y:
        if x in y:
            dicionario[x]=str.count(frases,x)
    return dicionario