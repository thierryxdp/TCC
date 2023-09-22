def conta_frases(texto):
    frase = 1
    if '.' in texto:
        frase = str.count(texto,'.')
    if '?' in texto:
        frase += str.count(texto,'?')
    if '!' in texto:
        frase += str.count(texto,'!')
    if '...' in texto:
        frase += str.count(texto,'...')*(-2)
    return frase