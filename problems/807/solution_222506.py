def conta_frases(texto):
    '''funçao conta o numero de frases que aparecem no texto'''
    '''str -> int'''
    
    a = str.count(texto,'...',0)
    b = str.count(texto,'.',0)
    c = str.count(texto,'?',0)
    d = str.count(texto,'!',0)
    e = str.count(texto,',',0)
    
    return a+b+c+d+e