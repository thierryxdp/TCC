def acima_da_media(notas):
    
    media=sum(notas)/len(notas)
    notas.append(media)
    list.sort(notas)
    local=list.index(notas,media)
    
    if notas[local]==notas[local+1]:
        return notas[local+1]