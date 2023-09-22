def acima_da_media(qualif):
    sum = 0
    for note in qualif:
        sum += note
        
    mean = sum / len(qualif)
    acima_da_media = bigger_than(qualif, mean)
    
    return mean, acima_da_media