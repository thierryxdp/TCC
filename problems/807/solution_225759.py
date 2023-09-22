def conta_frases(texto):
    'dado um texto retorne a queantidade de frases deste texto.str-->int'
    if '.' in texto:
        texto= str.split(texto,'.')
    if '!' in texto:
        texto= str.split(texto,'!')
    if '?' in texto:
        texto= str.split(texto,'?')
    if '...' in texto:
        texto= str.split(texto,'...')
    return len(texto)