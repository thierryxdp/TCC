def acima_da_media(lista):
    
    media = sum(lista)/len(lista)
    
    lista1 = lista + [media]
    list.sort(lista1)
    indice = list.index(lista1, media)
    lista2 = lista1[indice + 1:]
    
    return lista2