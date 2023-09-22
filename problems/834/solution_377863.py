def media_matriz(lista):
    
    i=0
    contador=0
    
    while i<len(lista):
        contador+=sum(lista[i])
        i+=1
    
    media= contador/(len(lista[0])*len(lista))
    
    return media