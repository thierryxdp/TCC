def conta_frases(texto):
    resultado=0
    if '...' in texto:
        resultado=str.count(texto, '...')
    if '.' in texto and '...' not in texto:
        resultado=resultado+str.count(texto, '.')
    if '.' in texto and '...' in texto:
        resultado=resultado+str.count(texto, '.')-3*(str.count(texto, '...'))
    if '?' in texto:
        resultado=resultado+str.count(texto, '?')
    if '!' in texto:
        resultado=resultado+str.count(texto,'!')
    return resultado