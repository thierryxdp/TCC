def conta_frases(texto):
    'conta a quantidade de frases que um texto possui str-> int'
    if '...' in texto:
        return str.count(texto, '.') + str.count(texto, '!') + str.count(texto, '?') + str.count(texto, '...') - 3*str.count(texto, '...')
    else:
        return str.count(texto, '.') + str.count(texto, '!') + str.count(texto, '?') + str.count(texto, '...')