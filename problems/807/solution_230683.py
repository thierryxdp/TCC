def conta_frases(x):
    
    return str.count(x,'.',0,1) + str.count(x, '!') + str.count(x,'?') + str.count(x, '...')