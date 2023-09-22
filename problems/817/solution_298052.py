def acima_da_media(lista):
    """Função que retorna uma lista ordenada com as 
    notas que ficaram acima da média
    list=>list"""
    
    soma = sum(lista)
    media = soma /len(lista)
    lista.insert(0,media)
    lista.sort()    
    indexdamedia = list.index(lista,media)
    #após pegar a posição da media na lista, é feito o fatiamento 
    #da mesma para pegar os nums maiores q a media
    listaF =lista[indexdamedia+1:]
    if listaF[0]==media:
        listaF.remove(media)
    return listaF