def conta_frases(texto):
    
    x=str.split(texto,'.')
    y=str.split(texto,'!')
    z=str.split(texto,'?')
    a=str.split(texto,'...')

    return len(a)