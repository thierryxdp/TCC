def acima_da_media(lista):
    """"""
    
    soma = sum(lista)
    media = soma /len(lista)
    lista.insert(0,media)
    lista.sort()
    indexdamedia = list.index(lista,media)
    listaF =lista[indexdamedia+1:]
    if listaF[0]==media:
        listaF.remove(listaF[0])
    return listaF