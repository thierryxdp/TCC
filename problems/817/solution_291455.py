def acima_da_media(notas):
    
    media = (sum(notas)) // (len(notas))
    notas.sort()
    acima = notas[media::]
    
    return media