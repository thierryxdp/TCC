def conta_frases(s):
    fpoint = str.replace(s,'...','.')
    phtype1 = str.count(fpoint,'.')
    phtype2 = str.count(s,'!')
    phtype3 = str.count(s,'?')
    
    phrases = phtype1 + phtype2 + phtype3
    return phrases