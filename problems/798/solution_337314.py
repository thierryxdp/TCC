def freq_palavras(frases):
    '''
    '''
    
    dicio={}
    frase2=frases.split()
    
    for palavra in frase2:
        if palavra in dicio:
            dicio[palavra]=palavra.count(frase2)
         
    return dicio