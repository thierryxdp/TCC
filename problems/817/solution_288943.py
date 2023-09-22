def acima_da_media(lista):
    
    media=sum(lista)/len(lista)
    
    lista2=[media]
    lista3=lista+lista2
    
    list.sort(lista3)
    n=list.index(lista3,media)
    y=list.count(lista3,media)
    lista4=lista3[(n+y):]

    return lista4