def conta_frases(texto):
    a= list.count(texto, '?')
    b= list.count(texto, '!')
    c= list.count(texto, '...')
    d= list.count(texto, '.')
    
    return len(a)+ len(b)+ len(c)+ len(d)