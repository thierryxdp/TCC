def acima_da_media(notas):
    "Retorne as notas acima da media das notas dadas;lista->lista"
    
    media=sum(notas)/len(notas)
    notas.append(media)
    list.sort(notas)
    x=notas.index(media)
    
    if media=sum(notas):
        return []
    else:
    
    return notas[x+1:]