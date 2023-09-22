def conta_frases(texto):
    frase = ('')
    if '.' in texto:
        frase = str.count(texto,'.')
    if '?' in texto:
        frase += str.count(texto,'?')
    if '!' in texto:
        frase += str.count(texto,'!')
    if '...' in texto:
        frase += str.count(texto,'...')*(-2)
    return frase