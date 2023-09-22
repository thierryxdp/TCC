def conta_frases(texto):
    x= texto.replace('...','.')
    a= x.replace('?','.')
    c= a.replace('!','.')
    cf= c.count('.')
    return cf