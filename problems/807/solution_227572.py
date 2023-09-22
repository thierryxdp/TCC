def conta_frases(texto):
    n=0
    i=0
    list(texto)
    while i<len(texto):
        if texto[i] == '.' or '!' or '?' or '...':
            n = n + 1
            return n
            
        i = 1 + i
        
    return n + 1