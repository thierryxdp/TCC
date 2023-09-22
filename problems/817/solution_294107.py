def acima_da_media(notas):
    
    media=sum(notas)/len(notas)
    notas.append(media)
    list.sort(notas)
    indice=list.index(notas,media)
    
    return notas[indice+1:]