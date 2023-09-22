def conta_frases(texto):
    '''...'''
    x = str.split(texto,'...')
    x = str.join('*',x)
    x = str.split(x,'?')
    x = str.join('*',x)
    x = str.split(x,'!')
    x = str.join('*',x)
    x = str.split(x,'.')
    x = str.join('*',x)
    return (len(str.split(x,'*')))-1