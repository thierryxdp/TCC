def freq_palavras(frases):
    '''
    '''
    i=0
    dicio={}
    frase2=frases.split()
    
    for palavra in frase2:
         dicio[palavra[i]]=palavra.count(frase2)
    
    return dicio