def acima_da_media(lista):
    """"""
    
    soma = sum(lista)
    media = soma /len(lista)
    lista.insert(media)
    lista.sort()
    indexdamedia = list.index(lista,media)
    
    return lista[indexdamedia+1:]