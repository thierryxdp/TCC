def freq_palavras(frases):
    
    dicio={}
    
    lista=frases.split(' ')
    
    for i in range(len(lista)):
        x=lista.count(lista[i])
        dicio[lista[i]]=x

    return dicio