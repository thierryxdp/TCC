def acima_da_media(lista):
    
    media = sum(lista)/len(lista)
    
    lista1 = lista + [media]
    list.sort(lista1)
    
    mult = list.count(lista1, media)
    indice = list.index(lista1, media)
    lista2 = lista1[indice + mult:]
    
    return lista2