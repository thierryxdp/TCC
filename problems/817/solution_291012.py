def acima_da_media(lista):
    
    media =  sum(lista)/len(lista) 
    lista1 = lista + [media]
    list.sort(lista1)
    if len(lista)%2 == 0:
        return lista1[len(lista)/2:]
    
    if len(lista)%2 <2:
        return lista1[int(len(lista)/2)+2:]