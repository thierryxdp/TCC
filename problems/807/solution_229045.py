def conta_frases(texto):
    
    ret = str.count(texto, str.join('*',str.split(texto,'...')))
    
    ponto = str.count(texto, ".")
    
    excl = str.count(texto, "!")
    
    inter = str.count(texto, "?")
    
    return ponto + excl + ret + inter