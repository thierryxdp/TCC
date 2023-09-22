def conta_frases(x):
    
    str.replace(x,'...','.')
    x
    
    return str.count(x,'.') + str.count(x,'...') + str.count(x,'!') + str.count(x,'?')