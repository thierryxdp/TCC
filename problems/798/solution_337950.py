def freq_palavras(frases):
    '''
    '''
    dicionario = {}
    y=str.split(frases)
    
    for x in y:
        for i in range(len(y[i])):
            if x in y:
                dicionario[x]=str.count(str(y[i]),x)
                
    return dicionario