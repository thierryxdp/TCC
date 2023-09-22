def conta_frases(texto):
    '''funçao conta o numero de frases que aparecem no texto'''
    '''str -> int'''
    
    a = str.count(texto,',')
    b = str.count(texto,'.')
    c = str.count(texto,'?')
    d = str.count(texto,'!')
    e = str.count(texto,'...')
    
    return str.join(a,b,c,d,e)