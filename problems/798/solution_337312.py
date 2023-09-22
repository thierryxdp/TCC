def freq_palavras(frases):
    '''
    '''
    
    dicio={}
    frase2=frase.split()
    
    for palavra in frase2:
        if palavra[i] in dicio:
            dicio[palavra]=palavra.count(frase2)
         
    return dicio