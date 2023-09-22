def acima_da_media(notas):
    
    media=sum(notas)/len(notas)
    lista=list.sort(notas)
    indice=list.index(lista,media)
    
    return notas[indice+1:]