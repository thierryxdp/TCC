def freq_palavras(frases):
    '''
    '''
    i=0
    dicio={}
    frase2=frases.split()
    
    for palavra in frase2:
         dicio[frase2[i]]=frase2.count(frase2[i])
    
    return dicio