def freq_palavras(frases):
    '''
    '''
    
    dicio={}
    
    for palavra in frases:
        if palavra in dicio:
            dicio[palavra]=palavra.count(frase)
            
        return dicio