def conta_frases(texto):
    
    x=str.split(texto,'.')
    x=str(x)
    y=str.split(x,'!')
    y=str(y)
    z=str.split(y,'?')
    z=str(z)
    a=str.split(z,'...')
    a=str(a)

    return len(a)