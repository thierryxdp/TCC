def conta_frases(texto):
    '''função que conta o numero de frases que aparece no texto;
    str->list'''
    if '...' in texto:
        str.split(texto,'...')
    if '.' in texto:
        str.split(texto,'.')
    if '!' in texto:
        str.split(texto,'!')
    if '?' in texto:
        str.split(texto,'?')
        return texto