def conta_frases(texto):
    if '.' in texto:
        frase = str.count(texto,'.')-3
    if '?' in texto:
        frase += str.count(texto,'?')
    if '!' in texto:
        frase += str.count(texto,'!')
    if '...' in texto:
        frase += str.count(texto,'...')
    
    return frase