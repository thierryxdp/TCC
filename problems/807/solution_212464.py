conta_frases(texto):
    '''Retorna o número de frases que contém em um texto
    str -> int'''
    t=str.count
    modelo=str.replace(texto,'.','...')
    trespontos=t(modelo,'...')
    pontoexc=t(modelo,'!')
    pontoint=t(modelo,'?')
    return trespontos+pontoexc+pontoint