def conta_frases(texto):
    
    x = str.count(texto,'. ')
    
    y = str.count(texto,'!')
    
    z = str.count(texto,'...')
    
    k = str.count(texto,'?')
    
    return x + y + z + k