def conta_frases(texto):
    if '.' in texto:
        frase1 = str.count(texto,'.')
    if '?' in texto:
        frase2 = str.count(texto,'?')
    if '!' in texto:
        frase3 = str.count(texto,'!')
    if '...' in texto:
        frase4 = str.count(texto,'...')*(-2)
    frase = frase1 + frase2 + frase3 + frase4
    return frase