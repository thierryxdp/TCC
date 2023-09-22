def acima_da_media(lista):
 
    media=round(sum(lista)/len(lista))
    
   	lista=list.append(media)
    list.sort(lista)
    list.reverse(lista)
   	indice=list.index(lista,media)
    lista_nova=lista[:indice-1]
    return lista_nova