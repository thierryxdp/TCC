def acima_da_media(lista):
    media=sum(lista)//len(lista)
    lista=lista+[media]
    
    list.sort(lista)
    list.reverse(lista)
    
    indice= list.index(lista,media)
    
    nova_lista=lista[:indice]
    list.reverse(nova_lista)
    return nova_lista