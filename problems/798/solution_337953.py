def freq_palavras(frases):
    '''
    '''
    dicionario = {}
    y=list(str.split(frases))
    
    for x in y:
        if x in y:
            dicionario[x]=str.count(str(y),x)
                
    return dicionario