def freq_palavras(frases):
    
    dicio={}
    
    lista=frases.split(' ')
    
    for i in range(len(lista)):
        dicio[frases[i]]=1
        
    return dicio