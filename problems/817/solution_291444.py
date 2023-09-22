def acima_da_media(notas):
    
    media = (sum(notas)) / (len(notas))
    notas.sort()
    notas[:media+1:-1] = []
    
    return notas