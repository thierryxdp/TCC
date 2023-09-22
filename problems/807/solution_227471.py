def conta_frases(texto):
    
    x=str.split(texto,'.')
    y=str.split(str(x),'!')
    z=str.split(str(y),'?')
    a=str.split(str(z),'...')

    return len(a)