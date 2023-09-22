def conta_frases(texto):
    x = str.count(texto, ".")
    y = str.count(texto, "!")
    z = str.count(texto, "?")
    j = str.count(texto, "...") 
    if j > 0:
        if j >= 1:
            j = j - (x-1)
            return x + y + z + j
        else:
            j = j - x
            return x + y + z + j
    
            
       
    else:
        return x + y + z + j