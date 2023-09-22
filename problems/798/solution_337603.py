def freq_palavras(frases):
    
    dicio={}
    
    lista=frases.split(' ')
    
    for i in range(len(lista)):
        dicio[lista[i]]+=1
        
    return dicio