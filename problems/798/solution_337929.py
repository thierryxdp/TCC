def freq_palavras(frases):
    '''
    '''
    dicionario = {}
    y=str.split(frases)
    
    for i in range(len(y)):
        if x[i] in y:
            dicionario[x[i]]=str.count(str(y),x[i])
    return dicionario