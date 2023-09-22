def acima_da_media(notas):
    
    media = (sum(notas)) / (len(notas))
    notas.append(media)
    notas.sort()
    cont = notas.index(media)
    
    if media == int:
        acima = notas[cont::]
        
    else:
        acima = notas[cont+2::]
    
    return acima