def conta_frases(texto):
    list(texto)
    i=0
    n=[]
    import string
    p = string.punctuation
    while i<len(texto):
        if texto[i] in p:
            n.append(texto[i])
            return len(n)
            
        i = i + 1
        
    return len(n)