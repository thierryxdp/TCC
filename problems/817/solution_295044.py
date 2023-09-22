def acima_da_media(notas):
    
    media = sum(notas)/len(notas)
    
    return notas[notas.index(media)+1:]