def conta_frases(texto):
    "Retorne o numero de frases de um dado texto; str->int"
    x=str.count(texto,'.')
    y=str.count(texto,'...')
    z=str.count(texto,'!')
    w=str.count(texto,'?')
    return (x+y+z+w)-(y/x)