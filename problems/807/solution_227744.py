def conta_frases(frases):
    x = str.count (frases, '...') 

    
    return str.count(frases, '.' or '!' or '?') - 2*x + x