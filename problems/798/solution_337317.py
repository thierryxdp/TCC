def freq_palavras(frases):
    '''
    '''
    i=0
    dicio={}
    frase2=frases.split()
    
    for palavra in frase2:
        if palavra[i] in dicio:
            dicio[palavra]=palavra.count(frase2)
    i+=1
    return dicio