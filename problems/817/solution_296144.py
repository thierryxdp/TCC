def acima_da_media(lista):
    
    list.sort(lista)
    list.reverse(lista)
    
    
    media=round(sum(lista)/len(lista))
    local=list.index(lista,media)
    
    lista= lista[local:]
    list.reverse(lista)
    return lista