def phrasecount(s):
    fpoint = str.replace(s,'...','.')
    phtypel = str.count(fpoint,'.')
    phtype2 = str.count(s,'!')
    phtype3 = str.count(s,'?')
    
    phrases = phtypel + phtype2 + phtype3 
    return phrases