def freq_palavras(frases):
    '''
    '''
    dicionario = {}
    for x in frases:
        if x in frases:
            dicionario={x:str.count(frases,"x")}
    return dicionario