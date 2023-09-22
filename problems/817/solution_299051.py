def acima_da_media(Lista):
    """Função que retorna uma lista ordenada com as notas acima da média.
    list => list"""
    
    soma = sum(Lista)
    Media = soma /len(Lista)
    Lista.insert(0,Media)
    Lista.sort()    
    indexdamedia = list.index(Lista, Media)
    #após pegar a posição da media na lista, é feito o fatiamento 
    #da mesma para pegar os nums maiores q a media
    listaF = lista[indexdamedia+1:]
    if listaF[0] == Media:
        listaF.remove(Media)
    return listaF