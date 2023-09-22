def freq_palavras(frases):
    '''
    '''
    dicionario = {}
    
    for x in frases:
        if x in frases:
            dicionario[x]=str.count(str.split(frases),x)
                
    return dicionario