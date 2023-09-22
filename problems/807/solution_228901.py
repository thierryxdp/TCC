def conta_frases(frases):
    
    return str.count(str.replace(frases,'...','.'),'.')+str.count(frases,'!')+str.count(frases,'?')