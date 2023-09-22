def conta_frases(frases):
    x = str.count (frases, '...') 

    
    return str.count(frases, '.' or '!' or '?' or '...') - 3*x + x