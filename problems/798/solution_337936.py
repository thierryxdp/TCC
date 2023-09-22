def freq_palavras(frases):
    '''
    '''
    dicionario = {}
    y=str.split(frases)
    
    for x in y:
        if x in y:
            dicionario[x]=str.count(str(y),x)
    return dicionario