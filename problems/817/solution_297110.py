def acima_da_media(lista):
    """"""
    
    soma = sum(lista)
    media = soma /len(lista)
    lista.insert(0,media)
    lista.sort()
    indexdamedia = list.index(lista,media)
    
    return lista[indexdamedia+1:]