def freq_palavras(frases):
    '''
    '''
    dicionario = {}
    y=str.split(frases)
    
    for i in range(len(y)):
        if x[i] in y:
            dicionario[x]=str.count(str(y),x)
    return dicionario