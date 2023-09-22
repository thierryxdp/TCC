def acima_da_media(lista):
 
    media=round(sum(lista)//len(lista))
    list.insert(lista,media)
   	indice=list.index(lista,media)
    
    return indice