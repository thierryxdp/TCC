def media_matriz(lista:list)->float:
    """função que calcula e retorna a média dos números
      de uma matriz com duas casas decimais de aproximação"""
    
    i=0
    contador=0
    
    while i<len(lista):
        contador+=sum(lista[i])
        i+=1
    
    media= contador/(len(lista[0])*len(lista))
    
    return round(media,2)