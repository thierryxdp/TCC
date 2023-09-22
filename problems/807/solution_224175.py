def conta_frases(texto):
    "Retorne o numero de frases de um dado texto; str->int"
    x=str.count(texto,'.'or'...')
    
    z=str.count(texto,'!')
    w=str.count(texto,'?')
    return x+z+w