def acima_da_media(notas):
    
    media = (sum(notas)) // (len(notas))
    notas.sort()
    notas[notas::-1] = []
    
    return notas