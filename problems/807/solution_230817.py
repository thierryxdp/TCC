def conta_frases(x):
    
    x = str.replace(x,'...','.')
    
    return str.count(x,'.') + str.count(x,'!') + str.count(x,'?')