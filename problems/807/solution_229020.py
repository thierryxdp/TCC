def conta_frases(texto):
    
    ponto = str.count(texto, ".")
    
    excl = str.count(texto, "!")
    
    ret = str.count(texto, "...")
    
    inter = str.count(texto, "?")
    
    return ponto + excl + ret + inter