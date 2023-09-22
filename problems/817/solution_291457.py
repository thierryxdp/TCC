def acima_da_media(notas):
    
    media = (sum(notas)) // (len(notas))
    notas.append(media)
    notas.sort()
    acima = notas[media+1::]
    
    return acima