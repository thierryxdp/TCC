def acima_da_media(lista):
    lista_numero = lista
    media = sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)
    
    indice = list.index(lista, media)
    
    return lista[indice+1:]