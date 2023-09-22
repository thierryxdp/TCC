def conta_frases(frases):
    x=frases.split('?')
    y=frases.split('.')
    w=frases.split('...')
    z=frases.split('!') 
    lista=(x+y+w+z)
    return lista.count(len(lista))