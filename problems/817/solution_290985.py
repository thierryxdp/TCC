def acima_da_media(lista):
    
    media =  sum(lista)/len(lista) 
    lista1 = lista + [media]
    list.sort(lista1)
    return lista1[media + 1:]