def acima_da_media(lista)
    
    media=(sum(lista))/len(lista)
    
    list.sort(lista)
    list.reverse(lista)
    
    indice= list.index(lista,n)
    
    nova_lista=lista[:media]
    list.reverse(nova_lista)
    return nova_lista