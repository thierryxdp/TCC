def conta_frases(texto):
    '''Retorna o numero de frases em um texto
    str --> int'''
    x = str.split(texto,'...')
    x = str.join('*',x)
    x = str.split(x,'?')
    x = str.join('*',x)
    x = str.split(x,'!')
    x = str.join('*',x)
    x = str.split(x,'.')
    x = str.join('*',x)
    return (len(str.split(x,'*')))-1