def conta_frases(texto):
    if '.' in texto:
        frase = str.count(texto,'.')-1
    if '?' in texto:
        frase += str.count(texto,'?')
    if '!' in texto:
        frase += str.count(texto,'!')
    if '...' in texto:
        frase += str.count(texto,'...')-2
    
    return frase