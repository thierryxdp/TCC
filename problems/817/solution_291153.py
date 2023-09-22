def acima_da_media(notas):
    
    notas.sort()
    media = sum(notas)/len(notas)
    if media not in notas:
    	notas.append(media)
    pos_media = notas.index(media)
    return notas[pos_media+1:]