def conta_frases(texto):
    '''conta o número de frases no texto de entrada terminada em: .!?...
    str->int'''
    if '...' in texto:
        texto = str.replace(texto,'...','.')
    if '!' in texto:
        texto = str.replace(texto,'!','.')
    if '?' in texto:
        texto = str.replace(texto,'?','.')
    return len(str.split(texto,'.'))-1