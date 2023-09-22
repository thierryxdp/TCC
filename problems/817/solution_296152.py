def acima_da_media(lista):
 
    media=sum(lista)/len(lista)
    
   	lista=lista+[media]
    list.sort(lista)
    list.reverse(lista)
   	indice=list.index(lista,media)
    lista_nova=lista[:indice]
    del lista[indice]
    return lista_nova