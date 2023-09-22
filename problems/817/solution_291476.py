def acima_da_media(notas):
    
    media = (sum(notas)) / (len(notas))
    notas.append(media)
    notas.sort()
    cont = notas.index(media)
    acima = notas[cont+1::]
    
    if media in acima:
        acima.remove(media)
        return acima
    
    else:
        return acima