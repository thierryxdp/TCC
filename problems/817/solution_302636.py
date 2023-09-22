def upper_mean(qualif):
    sum = 0
    for note in qualif:
        sum += note
        
    mean = sum / len(qualif)
    upper_mean = bigger_than(qualif, mean)
    
    return mean, upper_mean