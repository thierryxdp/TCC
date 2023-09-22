def conta_frases(string):
    a = str.count(string,'...')
    [Lstring] = string
    list.remove(Lstring,'...')
    b = str.count(string,'.')
    c = str.count(string,'!')
    d = str.count(string,'?')
    
    return a+b+c+d