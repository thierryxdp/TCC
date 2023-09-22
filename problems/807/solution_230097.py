def conta_frase(texto):
    if '.' in texto:
        frase = str.count(texto,'.')
    if '?' in texto:
        frase += str.count(texto,'?')
    if '!' in texto:
        frase += str.count(texto,'!')
    if '...' in texto:
        frase += str.count(texto,'...')
    return frase